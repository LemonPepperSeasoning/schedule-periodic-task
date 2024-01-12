import threading, time, os
from concurrent.futures import ProcessPoolExecutor
from task import task, TASK_FREQUENCY

def callback_function(future, task_id):
    print(f"Callback for Task {task_id}: Hello")


def main():
    print(f"You have #{os.cpu_count()} CPUs")
    print("* Starting task ...")
   
    with ProcessPoolExecutor() as executor:

        while True:
            start_time = time.monotonic()
        
            # Submit tasks to the process pool
            futures = executor.submit(task, "my-param")
            futures.add_done_callback(lambda f: print("finished a task"))

            elapsed_time = time.monotonic() - start_time
            sleep_time = max(0, TASK_FREQUENCY - elapsed_time)
            time.sleep(sleep_time)
        


    print("* Finished task")


if __name__ == "__main__":
    main()

