from epubmeta.meta import Metadata

class Ebook:
    def __init__(self, path):
        self.path = path

    def get_metadata(self):
        metadata = Metadata(self.get_opf())
