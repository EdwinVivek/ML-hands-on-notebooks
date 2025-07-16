import asyncio

async def long_task():
    print("Long task started...")
    await asyncio.sleep(10)
    print("Long task finished!")
    await asyncio.sleep(3)
    return "Done"

async def short_task():
    print("Short task started...")
    await asyncio.sleep(3)
    print("Short task finished!")

async def main():
    await asyncio.gather(long_task(), short_task())

async def main2():
    long_task_future = asyncio.create_task(long_task())  # Runs in background
    await short_task()  # Runs immediately
    result = await long_task_future  # Get the long task result when ready
    print(f"Long task result: {result}")

asyncio.run(main2())

