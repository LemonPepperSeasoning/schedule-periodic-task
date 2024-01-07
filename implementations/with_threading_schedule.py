import threading
import time

def your_function():
    # Your code here
    print(f"{time.time()} - Job executed")

def run_function_every_second():
    while True:
        start_time = time.time()
        your_function()
        elapsed_time = time.time() - start_time
        sleep_time = max(0, 1 - elapsed_time)
        time.sleep(sleep_time)

if __name__ == "__main__":
    threading.Thread(target=run_function_every_second).start()

