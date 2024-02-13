import time
import asyncio


from functools import wraps

from company_data import data


def timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = await func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"Время выполнения: {end:.4f} секунд")
        return res

    return wrapper


async def call_company(company_info: dict):
    _time = company_info.get("call_time")
    # seconds = 0
    print(
        f"Таска {asyncio.current_task().get_name()} запущена и будет выполняться {_time} сек"
    )

    await asyncio.sleep(_time)

    print(
        f"Company {company_info.get('Name')}: {company_info.get('Phone')} дозвон успешен"
    )

@timer
async def main():
    tasks = [asyncio.create_task(call_company(company)) for company in data]
    # await asyncio.sleep(6)
    _, pend = await asyncio.wait(tasks, timeout=6)
    print("*" * 50, "Не ответившие компании", "*" * 50, sep="\n")
    for task in tasks:
        if not task.done():
            # company = task.get_coro().cr_frame.f_locals["company_info"]
            task.cancel()
            print(task.get_coro().cr_frame.f_locals)
            # try:
            #     await task
            # except asyncio.CancelledError:

            # name = company["Name"]
            # phone = company["Phone"]
                # print(f"Таска {task.get_name()} отменена")
            # print(f"Компания {name}: {phone} не ответила")



if __name__ == "__main__":
    asyncio.run(main())
