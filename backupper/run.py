import subprocess

import arrow
from bypy import ByPy


def main():
    archive_name = 'archive-' + arrow.now().format('YYYYMMDD') + '.7z'
    snyc_folder = '/sync/'
    backup_folder = '/backup/'
    subprocess.run(['7z', 'a', snyc_folder + archive_name, backup_folder])
    bp = ByPy()
    bp.syncup(localdir=snyc_folder, remotedir=snyc_folder)


if __name__ == '__main__':
    main()
