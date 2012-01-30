"""TODO: description."""

import logging
import os.path
from zipfile import ZipFile
import epubmeta

log = logging.getLogger('backup')

def run():
    """Run this action."""

    path = epubmeta.arguments.filename
    backup_filename = os.path.basename(path)
    found_backup = False

    with ZipFile(path, 'r') as zip:
        names = zip.namelist()
        for parts in [m.split('/') for m in zip.namelist()]:
            if parts[:2] == ['META-INF', 'source'] and len(parts) > 2:
                found_backup = True
                break

        log.debug("Found existing backup: %s", found_backup)

        #if arguments.source:
        #    zip.write(getFN("zip"), "META-INF/source/mdepub_source.zip")
        metadata = zip.read("content.opf")

    if found_backup:
        log.debug("Skipping backup because a backup was found in the Epub package in \"META-INF/source/\".")
        return

    with open(path, 'r') as f:
        backup_data = f.read()

    backup_file_zippath = "META-INF/source/" + backup_filename
    with ZipFile(path, 'a') as zip:
        zip.writestr(backup_file_zippath, backup_data)

    log.debug("Wrote backup file \"%s\" inside Epub package.", backup_file_zippath)