import time
from task import task, TASK_FREQUENCY


def main():
    counter = 0

    while True:
        start_time = time.monotonic()
        task(counter)
        counter += 1
        elapsed_time = time.monotonic() - start_time
        sleep_time = max(0, TASK_FREQUENCY - elapsed_time)
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()

