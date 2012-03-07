"""Methods for manipulating an ebook file."""

import logging
from ebmeta.opfreader import Opf
#from epubmeta.ebook import *

log = logging.getLogger('ebook')

class Ebook(object):
    def __init__(self, path):
        self.path = path

    def __get_content_opf_str(): raise NotImplementedError()
    content_opf_str = property(fget=__get_content_opf_str,
        doc="""content.opf from ebook file as XML string."""
    )

    opf = property(
        fget=lambda self: Opf(self.content_opf_str),
        doc="""Metadata object with values populated from ebook file."""
    )

# Factory function:

import epub
import mobi
import pdf

def ebook_factory(path):
    ext = path.split(".")[-1].lower()

    logging.debug("filename extension: %s", ext)
    if ext == "epub": return epub.Epub(path)
    if ext == "mobi": return mobi.Mobi(path)
    if ext == "pdf": return pdf.Pdf(path)

    raise ValueError("Not a supported file type.")
