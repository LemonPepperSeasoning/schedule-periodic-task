import sched, time, threading
from task import task, TASK_FREQUENCY, TASK_PRIORITY


def main():

    LAG = 2

    start_time = round(time.monotonic())
    counter = 0

    while True:
        s = sched.scheduler(time.monotonic, time.sleep)

        for _ in range(5):
            s.enterabs(
                start_time + counter + LAG,
                TASK_PRIORITY,
                task,
                argument=(counter,)
            )

            counter += TASK_FREQUENCY

        scheduler_thread = threading.Thread(target=s.run)
        scheduler_thread.start()
        time.sleep(5)


if __name__ == "__main__":
    main()
