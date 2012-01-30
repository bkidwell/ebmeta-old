"""`epubmeta` is a tool for editing metadata in an Epub file.."""

import logging
import sys
import yaml
import epubmeta
import epubmeta.actions

def main():
    log = logging.getLogger('__main__')

    epubmeta.init()

    log.debug("Arguments: %s", repr(epubmeta.arguments))

    if epubmeta.arguments.action:
        getattr(epubmeta.actions, epubmeta.arguments.action).run()

if __name__ == '__main__':
    main()
