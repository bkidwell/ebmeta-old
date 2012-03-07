"""Reset metadata back to what it was before the first edit."""

import logging
import yaml
from zipfile import ZipFile
import ebmeta
from ebmeta import shell
from ebmeta.meta import Metadata
from ebmeta.actions import edit

log = logging.getLogger('display')

def run():
    """Run this action."""

    path = ebmeta.arguments.filename

    with ZipFile(path, 'r') as zip:
        yaml_text = zip.read("META-INF/original_metadata.yaml")

    edit.run(yaml_text)
