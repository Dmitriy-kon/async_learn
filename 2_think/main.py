import asyncio


async def normal_coro():
    print("this is normal coro")
    await asyncio.sleep(1)


async def func_with_error():
    print("func with error start")
    await asyncio.sleep(1)
    raise ValueError("Function error")


async def main():
    try:
        print("start main")
        coro = [func_with_error(), normal_coro()]
        await asyncio.gather(*coro)
        print("end main")
    except* ValueError as e_:
        for ex in e_.exceptions:
            print(f"{ex=}")
    else:
        print("All fine")


if __name__ == '__main__':
    asyncio.run(main())
