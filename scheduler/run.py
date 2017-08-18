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
            volumes[key] = {
                'bind': '/backup/' + val,
                'mode': 'rw',
            }
    print(client.containers.run('backupper', volumes=volumes))


def main():
    schedule.every().day.at('23:00').do(backup_job)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()
