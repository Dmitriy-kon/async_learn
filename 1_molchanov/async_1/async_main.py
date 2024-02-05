import asyncio


async def one():
    await asyncio.sleep(0)
    return 1


async def greet():
    await asyncio.sleep(1)
    return "hello world"


async def main():
    res1 = await one()
    res2 = await greet()

    print(res1)
    print(res2)


async def c():
    return 1


# task1 = asyncio.create_task(c())


asyncio.run(main())
