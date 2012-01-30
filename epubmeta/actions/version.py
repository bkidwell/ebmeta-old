"""Print epubmeta version number."""

import sys
import epubmeta

def run():
    print "{} {}".format(epubmeta.PROGRAM_NAME, epubmeta.VERSION)
    sys.exit(0)
