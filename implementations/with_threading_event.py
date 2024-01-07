import threading, time
from task import task, TASK_FREQUENCY


def main():
    ticker = threading.Event()
    while not ticker.wait(TASK_FREQUENCY):
        task()


if __name__ == "__main__":
    main()

