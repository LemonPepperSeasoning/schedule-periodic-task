import threading, time
from task import task, TASK_FREQUENCY


def run_function_every_second():
    while True:
        start_time = time.time()
        task()
        elapsed_time = time.time() - start_time
        sleep_time = max(0, TASK_FREQUENCY - elapsed_time)
        time.sleep(sleep_time)


if __name__ == "__main__":
    threading.Thread(target=run_function_every_second).start() # run on diff thread

