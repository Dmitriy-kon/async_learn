import asyncio


async def one():
    return 1


async def greet(timeout):
    await asyncio.sleep(timeout)
    return f"hello world {timeout}"


async def main():
    res1 = asyncio.create_task(one())
    res2 = asyncio.create_task(greet(6))
    res3 = asyncio.create_task(greet(4))
    res4 = asyncio.create_task(greet(3))

    print(await res1)
    print(await res2)
    print(await res3)
    print(await res4)


asyncio.run(main())
