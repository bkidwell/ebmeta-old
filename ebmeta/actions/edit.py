"""Edit metadata using zenity."""

from BeautifulSoup import BeautifulStoneSoup, Tag
import logging
import yaml
from zipfile import ZipFile
import ebmeta
from ebmeta import shell
from ebmeta.actions import backup
from ebmeta.ebook import ebook_factory
from ebmeta.meta import Metadata
import zenity

log = logging.getLogger('display')

def run(new_yaml_text=None):
    """Run this action."""

    path = ebmeta.arguments.filename
    ebook = ebook_factory(path)
    metadata = ebook.metadata
    yaml_text = metadata.yaml()

    if new_yaml_text:
        result = new_yaml_text
    else:
        try:
            result = zenity.edit_string(yaml_text)
        except zenity.ZenityCancelled:
            log.debug("Operation was cancelled.")
            return

    if result.strip() == yaml_text.strip():
        log.debug("No change was made.")
    elif result:
        log.debug("Writing changes to Epub file.")
        d1 = yaml.load(yaml_text)
        d2 = yaml.load(result)
        if not d2.get('uuid'):
            # ensure the new metadata has a uuid
            d2['uuid'] = ebmeta.new_id()
        changes = dict()
        for key in d2.keys():
            if key == 'description':
                if d1[key].strip() != d2[key].strip(): changes[key] = d2[key]
            else:
                if d1[key] != d2[key]: changes[key] = d2[key]
        log.debug("The following keys changed: %s", ' '.join(changes.keys()))

        backup.run() # backup only if backup doesn't exist
        with ZipFile(path, 'a') as zip:
            # backup metadata found in content.opf, for 'reset' action
            names = zip.namelist()
            found_metadata = False
            for member in zip.namelist():
                if member == "META-INF/original_metadata.yaml":
                    found_metadata = True
                    break
            if not found_metadata:
                zip.writestr("META-INF/original_metadata.yaml", yaml_text)

        writeChanges(changes)

def writeChanges(changes):
    """Write the metadata in the given dictionary into the Epub file."""

    path = ebmeta.arguments.filename

    for key in changes.keys():
        if changes[key] == None: changes[key] = ""

    args = [
        "ebook-meta",
        '"{}"'.format(path)
    ]
    for a, b in (
        ('author-sort',   'author sort'),
        ('authors',       'authors'),
        ('book-producer', 'book producer'),
        ('isbn',          'isbn'),
        ('language',      'language'),
        ('pubdate',       'publication date'),
        ('publisher',     'publisher'),
        ('rating',        'rating'),
        ('series',        'series'),
        ('series-index',  'series index'),
        ('title-sort',    'title sort'),
    ):
        if changes.has_key(b): args.append("--{}=\"{}\"".format(a, quote(changes[b])))

    if changes.has_key('description'):
        description = shell.pipe(["pandoc"], changes['description'])
        args.append(  "--comments=\"{}\"".format(quote(description))  )

    if changes.has_key('tags'):
        args.append(  "--tags=\"{}\"".format(quote(','.join(changes['tags'])))  )

    if len(args) > 2:
        # Run ebook-meta
        shell.run(" ".join(args), shell=True)

    if(changes.has_key('uuid')): setUuid(changes['uuid'])

def setUuid(uuid_txt):
    """Write a new uuid to the Epub file."""

    path = ebmeta.arguments.filename

    metadata = None
    metapath = "content.opf"
    with ZipFile(path, 'r') as zip:
        try:
            metadata = zip.read(metapath)
        except KeyError:
            metapath = "OEBPS/content.opf"
            metadata = zip.read(metapath)

    log.debug("new uuid: %s", uuid_txt)

    soup = BeautifulStoneSoup(metadata)
    id = (
        soup.find('dc:identifier', attrs={'opf:scheme':'uuid'}) or
        soup.find('dc:identifier', attrs={'opf:scheme':'UUID'}) or
        soup.find('dc:identifier', attrs={'scheme':'uuid'}) or
        soup.find('dc:identifier', attrs={'scheme':'UUID'})
    )
    if not id:
        m = soup.find('metadata')
        id = Tag(soup, 'dc:identifier')
        id['id'] = 'uuid_id'
        id['opf:scheme'] = 'uuid'
        id.insert(0, "--")
        m.insert(0, id)
    id.contents[0].replaceWith(unicode(uuid_txt))

    #[node.extract() for node in id.findAll()] # remove contents
    #id.insert(0, uuid) # insert uuid

    shell.run(["zip", "-d", path, metapath])
    with ZipFile(path, 'a') as zip:
        zip.writestr(metapath, str(soup))

def quote(text):
    """Change " to \\"."""

    return unicode(text).replace('"', '\\"')
