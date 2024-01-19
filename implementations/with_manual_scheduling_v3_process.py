import time
from concurrent.futures import ProcessPoolExecutor
from task import task, TASK_FREQUENCY


def main():
    counter = 0
    start_time = round(time.monotonic())

    with ProcessPoolExecutor() as executor:
        while True:
            _ = executor.submit(task, counter)
            elapsed_time = time.monotonic() - start_time - counter
            sleep_time = max(0, TASK_FREQUENCY - elapsed_time)
            time.sleep(sleep_time)
            counter += 1


if __name__ == "__main__":
    main()

