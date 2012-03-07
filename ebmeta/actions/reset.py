"""Reset metadata back to what it was before the first edit."""

import logging
import os
import os.path
import shutil
import ebmeta

log = logging.getLogger('display')

def run():
    """Run this action."""

    path = ebmeta.arguments.filename
    abspath = os.path.abspath(path)
    folder = os.path.dirname(abspath)

    backup_folder = os.path.join(folder, ".backup")
    backup_path = os.path.join(
        backup_folder, os.path.basename(path) + ".backup"
    )

    if not os.path.exists(backup_path):
        print "Backup file not found in \"{}\". Can't restore metadata.".format(backup_path)
        exit(1)

    shutil.copy2(backup_path, abspath)
    log.debug("Restored \"{}\" from backup.".format(abspath))
