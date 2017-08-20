import subprocess
import os

import arrow
from bypy import ByPy


def main():
    prefix = os.getenv('ARCHIVE_NAME_PREFIX', 'archive')
    archive_name = prefix + '-' + arrow.now().format('YYYYMMDD') + '.7z'
    snyc_folder = '/sync/'
    backup_folder = '/backup/'
    run_arguments = ['7z', 'a', snyc_folder + archive_name, backup_folder]
    # set password if needed
    archive_pass = os.getenv('ARCHIVE_PASS', '')
    if archive_pass:
        run_arguments.append('-p' + archive_pass)
    subprocess.run(run_arguments)
    bp = ByPy()
    bp.syncup(localdir=snyc_folder, remotedir=snyc_folder)


if __name__ == '__main__':
    main()
