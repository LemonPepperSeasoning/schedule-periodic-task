import asyncio, time
from task import async_task, TASK_FREQUENCY


async def schedule_job(interval_seconds):
    while True:
        await asyncio.sleep(interval_seconds)
        asyncio.create_task(async_task())


async def main():
    # Set the interval for the job (e.g., every 5 seconds)

    # Schedule the job
    await schedule_job(TASK_FREQUENCY)


if __name__ == "__main__":
    asyncio.run(main())

