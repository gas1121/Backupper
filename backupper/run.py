import schedule
import time


def backup_job():
    pass


def main():
    schedule.every().day.at('23:00').do(backup_job)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()
