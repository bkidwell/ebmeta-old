"""Display metadata from FILE"""

import logging
import ebmeta
from ebmeta.meta import Metadata
from ebmeta.ebook import ebook_factory

log = logging.getLogger('display')

def run():
    """Run this action."""

    path = ebmeta.arguments.filename
    ebook = ebook_factory(path)
    print unicode(ebook.metadata)
