import time, threading
from task import task, TASK_FREQUENCY
from concurrent.futures import ThreadPoolExecutor
import os



def main():
    counter = 0
    start_time = round(time.monotonic())
    
    print(f"Creating threadpool of size #{os.cpu_count()}")

    with ThreadPoolExecutor() as executor:
        while True:
            _ = executor.submit(task, args=(counter,))
            elapsed_time = time.monotonic() - start_time - counter
            sleep_time = max(0, TASK_FREQUENCY - elapsed_time)
            time.sleep(sleep_time)
            counter += 1


if __name__ == "__main__":
    main()

