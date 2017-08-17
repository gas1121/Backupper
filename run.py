import schedule
import docker
import time
import os


def backup_job():
    """
    mount target named volumes and dir to backupper container and
    generate a compressed package
    """
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    backupper_path = os.getcwd() + '/backupper'
    # TODO read volume and folder form file every time
    volumes = {
        'backupper_bypy': {'bind': '/root/.bypy', 'mode': 'rw'},
        backupper_path: {'bind': '/app', 'mode': 'rw'},
        'japancinemastatusspider_pgdata': {'bind': '/backup/pgdata',
                                           'mode': 'rw'},
    }
    print(client.containers.run('backupper', volumes=volumes))


def main():
    schedule.every().day.at('23:00').do(backup_job)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()
