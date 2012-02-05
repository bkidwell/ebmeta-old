"""Methods for manipulating an ebook file."""

import logging
import epub
#from epubmeta.ebook import *

log = logging.getLogger('ebook')

def ebook_factory(path):
    ext = path.split(".")[-1].lower()

    logging.debug("filename extension: %s", ext)
    if ext == "epub": return epub.Epub(path)

    #if ext == "epub": self.type = "epub"
    #elif ext == "pdf": self.type = "pdf"
    #elif ext == "mobi": self.type = "mobi"
    #else: self.type = None
