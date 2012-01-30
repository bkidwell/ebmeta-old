"""Assign a new ID for this Epub file."""

import logging
import re
import epubmeta
from epubmeta import new_id

log = logging.getLogger('newid')

r_uuid = re.compile(
    r'^([ \t]*)uuid:([ \t]*)([\S]*)([ \t]*)$',
    re.MULTILINE
)

def run():
    """Run this action."""
