"""
ebmeta package
"""

VERSION = "0.1"
PROGRAM_NAME = "ebmeta"

arguments = None # global container for command line arguments
log = None

import logging
import os
import sys
import uuid
from ebmeta.argumentparser import ArgumentParser

def new_id():
    """Generate a new random UUID"""

    return uuid.uuid4()

def init():
    """Initialize epubmeta package."""

    global arguments
    global log

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('ebmeta')

    project_path = os.getcwd()
    log.debug("Working path: %s", project_path)

    arguments = ArgumentParser().parse_args()
