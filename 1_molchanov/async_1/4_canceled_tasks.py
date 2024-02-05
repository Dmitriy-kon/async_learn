import asyncio


async def greet(timeout):
    await asyncio.sleep(timeout)
    return f"hello world {timeout}"


async def main():
    long_task = asyncio.create_task(greet(20))

    seconds = 0

    while not long_task.done():
        await asyncio.sleep(1)
        seconds += 1

        if seconds == 5:
            long_task.cancel()

        print(f"Time passed {seconds}")

    try:
        await long_task
    except asyncio.CancelledError as er_:
        print(f"To long task {er_}")


asyncio.run(main())
