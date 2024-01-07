import threading, time
from task import task, TASK_FREQUENCY


def main():
    print("* Starting task ...")
    
    while True:
        start_time = time.monotonic()
        threading.Thread(target=task).start()
        elapsed_time = time.monotonic() - start_time
        sleep_time = max(0, TASK_FREQUENCY - elapsed_time)
        time.sleep(sleep_time)

    print("* Finished task")


if __name__ == "__main__":
    main()

