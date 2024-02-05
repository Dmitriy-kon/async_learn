import asyncio

import asyncio
import aiohttp


async def coro_norm():
    return "Hello world"


async def coro_value_error():
    raise ValueError


async def coro_type_error():
    raise TypeError


async def coro_long():
    try:
        print('Long task in running...')
        await asyncio.sleep(2)
        print('Long task in completed')
        return 'Long task'

    except asyncio.CancelledError as e:
        print("All needed actions are done")
        raise asyncio.CancelledError


async def main():
    task1 = asyncio.create_task(coro_norm())
    task2 = asyncio.create_task(coro_value_error())
    task3 = asyncio.create_task(coro_long(), name='Coro long')

    tasks = [task1, task2, task3]

    try:
        results = await asyncio.gather(*tasks)

    except ValueError as e:
        print(f"{e=}")
    else:
        print(f"{results=}")

    for task in tasks:
        if not task.done():
            task.cancel()
            print(f"Таска {task.get_name()} отменена")

    # try:
    #     async with asyncio.TaskGroup() as tg:
    #         res1 = tg.create_task(coro_norm())
    #         res2 = tg.create_task(coro_type_error())
    #         res3 = tg.create_task(coro_value_error())
    #
    #     results = [res1.result(), res2.result(), res3.result()]
    #
    # except* ValueError as e:
    #     print(f"{e=}")
    # except* TypeError as e:
    #     print(f"{e=}")
    # else:
    #     print(f"{results=}")


asyncio.run(main())
