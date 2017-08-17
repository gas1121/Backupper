import os
import subprocess


def main():
    subprocess.run(['7z', 'a', 'archive.7z', '/backup/pgdata'])


if __name__ == '__main__':
    main()
