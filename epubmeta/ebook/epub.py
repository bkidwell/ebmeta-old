import logging
from zipfile import ZipFile
import ebook

log = logging.getLogger('epub')

class Epub(ebook.Ebook):
    def __init__(self, path):
        self.type = 'epub'
        self.__content_opf = None
        super(Epub, self).__init__(path)

    def __get_content_opf(self):
        if self.__content_opf: return self.__content_opf

        with ZipFile(self.path, 'r') as zip:
            try:
                self.__content_opf = zip.read("content.opf")
            except KeyError:
                self.__content_opf = zip.read("OEBPS/content.opf")
        return self.__content_opf

    content_opf = property(__get_content_opf)