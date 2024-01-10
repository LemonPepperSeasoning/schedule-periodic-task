import threading, time
from task import task, TASK_FREQUENCY


def main():
    ticker = threading.Event()
    counter = 0

    while not ticker.wait(TASK_FREQUENCY):
        task(counter)
        counter += 1


if __name__ == "__main__":
    main()

