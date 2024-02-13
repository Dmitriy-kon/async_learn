import asyncio

from company_data import data


async def call_company(company_info: dict):
    _time = company_info.get("call_time")
    # seconds = 0
    print(
        f"Таска {asyncio.current_task().get_name()} запущена и будет выполняться {_time} сек"
    )

    await asyncio.sleep(_time)

    if _time > 5:
        asyncio.current_task().cancel()
        print(f"Таска {asyncio.current_task().get_name()} отменена")
        raise asyncio.CancelledError(company_info)

    print(
        f"Company {company_info.get('Name')}: {company_info.get('Phone')} дозвон успешен"
    )


async def main():
    tasks = [asyncio.create_task(call_company(company)) for company in data]
    cancelled_task = []
    await asyncio.sleep(6)

    for task in tasks:
        if not task.done():
            task.cancel()
            # print(task)
            cancelled_task.append(task)

    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError as e:
        print()
        print("*" * 50)
        print()
        for task in cancelled_task:
            print(type(task.get_coro().cr_frame), e.args)
            # company = task.get_coro().cr_frame.f_locals["company_info"]
            # print(f"Компания {company['Name']}: {company['Phone']} не ответила")
        # print(f"Таска {asyncio.current_task().get_name()} отменена")


if __name__ == "__main__":
    asyncio.run(main())
