"""Module for handling epubmeta command line arguments."""

import argparse
import logging
import textwrap
import epubmeta

log = logging.getLogger('argumentparser')

help="""\
TODO: Description
"""

epilog="""\
actions:
  backup       Backup FILE.EPUB to an embedded file inside FILE.EPUB
  display      Display metadata from FILE.EPUB
  newid        Assign a new UUID to this EPUB file
  version      Print epubmeta version number

"""

def setup_args(parser):
    """Add epubmeta argument structure to an instance of ArgumentParser."""

    parser.add_argument(
        'action', nargs='?', metavar='action',
        choices=['backup', 'display', 'newid', 'version'],
        help="Which action to perform."
    )
    parser.add_argument(
        'filename', nargs='?', metavar='FILE.EPUB',
        help="Path to an EPUB file."
    )

class ArgumentParser(argparse.ArgumentParser):
    """Extend argparse.ArgumentParser with the argument structure for mdepub."""

    def __init__(self):
        super(ArgumentParser, self).__init__(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=help, epilog=epilog, prog=epubmeta.PROGRAM_NAME
        )
        setup_args(self)
