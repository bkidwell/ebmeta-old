import logging
from zipfile import ZipFile
import ebook

log = logging.getLogger('epub')

print ebook.ebook_factory

class Epub(ebook.Ebook):
    def __init__(self, path):
        self.type = 'epub'
        super().__init__(path)

    def get_opf(self):
        if self.content_opf: return self.content_opf

        with ZipFile(path, 'r') as zip:
            try:
                self.content_opf = zip.read("content.opf")
            except KeyError:
                self.content_opf = zip.read("OEBPS/content.opf")
        return self.content_opf
