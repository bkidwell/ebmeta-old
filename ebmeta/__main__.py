"""`epubmeta` is a tool for editing metadata in an Epub file.."""

import logging
import sys
import yaml
import ebmeta
import ebmeta.actions

def main():
    log = logging.getLogger('__main__')

    ebmeta.init()

    log.debug("Arguments: %s", repr(ebmeta.arguments))

    if ebmeta.arguments.action:
        getattr(ebmeta.actions, ebmeta.arguments.action).run()

if __name__ == '__main__':
    main()
