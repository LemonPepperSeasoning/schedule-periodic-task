import time, threading
from task import task, TASK_FREQUENCY


def main():
    counter = 0
    start_time = round(time.monotonic())

    while True:
        threading.Thread(target=task, args=(counter,)).start()
        elapsed_time = time.monotonic() - start_time - counter
        sleep_time = max(0, TASK_FREQUENCY - elapsed_time)
        time.sleep(sleep_time)
        counter += 1


if __name__ == "__main__":
    main()
