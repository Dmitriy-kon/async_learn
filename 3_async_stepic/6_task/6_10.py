import asyncio

async def foo():
    await asyncio.sleep(1)
    print("foo")

async def main():
    task = asyncio.create_task(foo())
    print(f"Корутина {task.get_coro()} создана")

asyncio.run(main())
