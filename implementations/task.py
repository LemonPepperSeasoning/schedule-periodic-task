import random, time


TASK_FREQUENCY = 1 # run task every N seconds
TASK_PRIORITY = 1


async def async_task():
    task()


def task(id = 0):
    print(f"Running task-{id:<10} - Monotonic: {time.monotonic():<18} - System: {time.time():<18}")
    time.sleep(random.random()) # Assume job task 0 ~ 1 seconds

