"""Methods for manipulating an ebook file."""

import logging
import epubmeta.ebook.epub
from epubmeta.meta import Metadata
#from epubmeta.ebook import *

log = logging.getLogger('ebook')

def ebook_factory(path):
    ext = path.split(".")[-1].lower()

    logging.debug("filename extension: %s", ext)
    if ext == "epub": return epubmeta.ebook.epub.Epub(path)

    #if ext == "epub": self.type = "epub"
    #elif ext == "pdf": self.type = "pdf"
    #elif ext == "mobi": self.type = "mobi"
    #else: self.type = None

class Ebook(object):
    def __init__(self, path):
        self.path = path

    def __get_content_opf(): raise NotImplementedError()
    content_opf = property(fget=__get_content_opf,
        doc="""Get content.opf as XML string"""
    )

    metadata = property(
        fget=lambda self: Metadata(self.content_opf),
        doc="""Get a metadata object with values populated from ebook file."""
    )
