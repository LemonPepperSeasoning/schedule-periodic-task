import time
from task import task, TASK_FREQUENCY


def main():
    counter = 0

    while True:
        task(counter)
        counter += 1
        time.sleep(TASK_FREQUENCY)


if __name__ == "__main__":
    main()

