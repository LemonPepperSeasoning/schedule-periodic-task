import asyncio, time

async def my_job():
    print(f"{time.monotonic()} - Job executed!")
    time.sleep(0.2)

async def schedule_job(interval_seconds):
    while True:
        await asyncio.sleep(interval_seconds)
        asyncio.create_task(my_job())


async def main():
    # Set the interval for the job (e.g., every 5 seconds)
    interval_seconds = 1

    # Schedule the job
    await schedule_job(interval_seconds)


if __name__ == "__main__":
    asyncio.run(main())

