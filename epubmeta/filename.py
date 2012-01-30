import unicodedata
import os.path
import string
import epubmeta

validFilenameChars = "'-_.() {}{}".format(string.ascii_letters, string.digits)

def clean(filename):
    """Clean filename of problematic characters."""

    cleanedFilename = unicodedata.normalize('NFKD', unicode(filename)).encode('ASCII', 'ignore')
    return ''.join(c for c in cleanedFilename if c in validFilenameChars)
