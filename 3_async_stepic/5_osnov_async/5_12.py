import asyncio

async def my_task():
    print("Task started")


async def main():
    loop = asyncio.get_running_loop()
    loop.create_task(my_task())
    await asyncio.sleep(1)
if __name__ == "__main__":
    asyncio.run(main())
