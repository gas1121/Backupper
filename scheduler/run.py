import schedule
import docker
import time


def backup_job():
    """
    mount target named volumes and dir to backupper container and
    generate a compressed package, then send it to BaiduYunNetDisk
    """
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    # read volume and folder form file every time
    volumes = {
        'backupper_bypy': {'bind': '/root/.bypy', 'mode': 'rw'},
    }
    with open('/data/data.txt', 'r') as f:
        for line in f:
            key, val = line.partition("=")[::2]
            if not key or not val:
                continue
            volumes[key] = {
                'bind': '/backup/' + val,
                'mode': 'rw',
            }
    # if no volume needs to backup, return
    if len(volumes) == 1:
        return
    client.containers.run('backupper', volumes=volumes)


def main():
    schedule.every().week().at('23:00').do(backup_job)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()
