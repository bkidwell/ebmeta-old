import logging
from zipfile import ZipFile
from . import Ebook

log = logging.getLogger('epub')

class Epub(Ebook):
    def __init__(self, path):
        self.type = 'epub'
        self.__content_opf_str = None
        super(Epub, self).__init__(path)

    def __get_content_opf_str(self):
        if self.__content_opf_str: return self.__content_opf_str

        with ZipFile(self.path, 'r') as zip:
            try:
                self.__content_opf_str = zip.read("content.opf")
            except KeyError:
                self.__content_opf_str = zip.read("OEBPS/content.opf")
        return self.__content_opf_str

    content_opf_str = property(__get_content_opf_str)