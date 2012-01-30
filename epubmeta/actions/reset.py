"""Reset metadata back to what it was before the first edit."""

import logging
import yaml
from zipfile import ZipFile
import epubmeta
from epubmeta import shell
from epubmeta.meta import Metadata
from epubmeta.actions import edit

log = logging.getLogger('display')

def run():
    """Run this action."""

    path = epubmeta.arguments.filename

    with ZipFile(path, 'r') as zip:
        yaml_text = zip.read("META-INF/original_metadata.yaml")

    edit.run(yaml_text)
