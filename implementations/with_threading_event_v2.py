import threading, time
from task import task, TASK_FREQUENCY


def main():
    ticker = threading.Event()

    start_time = time.monotonic()
    counter = 0

    while not ticker.wait(1 - time.monotonic() + start_time + counter):
        task(counter)
        counter += 1


if __name__ == "__main__":
    main()

