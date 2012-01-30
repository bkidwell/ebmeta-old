"""Display an Epub file's metadata."""

import logging
from zipfile import ZipFile
import epubmeta
from epubmeta.meta import Metadata

log = logging.getLogger('display')

def run():
    """Run this action."""

    path = epubmeta.arguments.filename
    with ZipFile(path, 'r') as zip:
        content_opf = zip.read("content.opf")

    metadata = Metadata(content_opf)
    print unicode(metadata)
