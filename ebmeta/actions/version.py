"""Print ebmeta version number."""

import sys
import ebmeta

def run():
    print "{} {}".format(ebmeta.PROGRAM_NAME, ebmeta.VERSION)
    sys.exit(0)
