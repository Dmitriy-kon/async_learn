import asyncio


async def busy_loop():
    for i in range(10):
        await nothing()


async def nothing():
    await asyncio.sleep(0)
    print('busy')


async def normal():
    for i in range(10):
        await asyncio.sleep(0)
        print('Normal coroutine')


async def main():
    # await asyncio.gather(
    #     busy_loop(),
    #     normal()
    # )

    res1 = asyncio.create_task(busy_loop())
    res2 = asyncio.create_task(normal())

    await res1
    await res2


asyncio.run(main())
