import time
from task import task, TASK_FREQUENCY


if __name__ == "__main__":
    while True:
        task()
        time.sleep(TASK_FREQUENCY)
