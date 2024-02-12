import asyncio

async def my_task(n):
    print(f"task {n} started")
    await asyncio.sleep(n)
    print(f"task {n} finished")

async def main():
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(my_task(i)) for i in range(1, 6)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())