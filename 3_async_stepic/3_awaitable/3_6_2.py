import asyncio


async def do_some_work_1(x):
    print(f"Выполнение работы 1: {x}")
    await asyncio.sleep(x)
    return x * 2

async def do_some_work_2(x):
    print(f"Выполнение работы 2: {x}")
    await asyncio.sleep(x)
    return x + 2

async def main():
    future = asyncio.ensure_future(do_some_work_1(2))
    result_1 = await future
    future2 = asyncio.ensure_future(do_some_work_2(result_1))
    result_2 = await future2
    print(f"Результат 1: {result_1}")
    print(f"Результат 2: {result_2}")
    
    
if __name__ == "__main__":
    asyncio.run(main())