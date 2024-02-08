import asyncio


async def my_coro():
    await asyncio.sleep(5)
    return "Hi its long coro"


async def main():
    task = asyncio.create_task(my_coro())
    try:
        await asyncio.wait_for(
            asyncio.shield(task), 
            # task, 
            timeout=2)
    
    except asyncio.TimeoutError:
        print("Timeout for coro")
        try:
            res = await task
            print(res)
        except asyncio.CancelledError:
            print("Cancelled")


if __name__ == "__main__":
    asyncio.run(main())
