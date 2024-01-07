import schedule, time
from task import task, TASK_FREQUENCY


def main():
    #schedule.every().day.at('13:56').do(sched_job)
    schedule.every(TASK_FREQUENCY).seconds.do(lambda: task("my param"))

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    main()

