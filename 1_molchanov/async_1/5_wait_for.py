import asyncio


async def greet(timeout):
    await asyncio.sleep(timeout)
    return f"hello world {timeout}"


async def main():
    long_task = asyncio.create_task(greet(5))

    try:
        result = await asyncio.wait_for(
            asyncio.shield(long_task),
            timeout=3
        )
    except asyncio.TimeoutError as er_:
        print(f"To long task {er_}")
        result = await long_task

        print(result)


asyncio.run(main())
