"""Display metadata from FILE.EPUB"""

import logging
import epubmeta
from epubmeta.meta import Metadata
from epubmeta.ebook import ebook_factory

log = logging.getLogger('display')

def run():
    """Run this action."""

    path = epubmeta.arguments.filename
    ebook = ebook_factory(path)
    print unicode(ebook.metadata)
