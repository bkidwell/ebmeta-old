"""Edit metadata using zenity."""

from BeautifulSoup import BeautifulStoneSoup, Tag
import logging
import yaml
from zipfile import ZipFile
import epubmeta
from epubmeta import shell
from epubmeta.meta import Metadata
from epubmeta.actions import backup

log = logging.getLogger('display')

def run(new_yaml_text=None):
    """Run this action."""

    path = epubmeta.arguments.filename

    with ZipFile(path, 'r') as zip:
        try:
            content_opf = zip.read("content.opf")
        except KeyError:
            content_opf = zip.read("OEBPS/content.opf")

    metadata = Metadata(content_opf)
    yaml_text = metadata.yaml()

    args = [
        'zenity',
        '--title', "Edit EPUB Metadata",
        '--width=700',
        '--height=550',
        '--text-info',
        # '--font=Monospace',
        '--editable'
    ]
    if new_yaml_text:
        result = new_yaml_text
    else:
        result = shell.pipe(args, yaml_text)

    if result.strip() == yaml_text.strip():
        log.debug("No change was made.")
    elif result:
        log.debug("Writing changes to Epub file.")
        d1 = yaml.load(yaml_text)
        d2 = yaml.load(result)
        if not d2.get('uuid'):
            # ensure the new metadata has a uuid
            d2['uuid'] = epubmeta.new_id()
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
    else:
        log.debug("Operation was cancelled.")

def writeChanges(changes):
    """Write the metadata in the given dictionary into the Epub file."""

    path = epubmeta.arguments.filename

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

    path = epubmeta.arguments.filename

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
    id = soup.find('dc:identifier', attrs={'opf:scheme':'uuid'})
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
