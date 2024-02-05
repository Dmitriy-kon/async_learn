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
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(coro_norm(), name='norm')
            task2 = tg.create_task(coro_value_error(), name='error')
            task3 = tg.create_task(coro_long(), name='long')

        results = [task1.result(), task2.result(), task3.result()]
        print(results)

    except* ValueError as e:
        for ex in e.exceptions:
            print(f"{ex=}")
    else:
        print(f"{results=}")
    #
    # for task in tasks:
    #     if not task.done():
    #         task.cancel()
    #         print(f"Pending: {task.get_name()}")
    #
    # print()
    #
    # await asyncio.sleep(2)
    # print(f"{task1._state}")
    # print(f"{task2._state}")
    # print(f"{tasl3._state}")

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
