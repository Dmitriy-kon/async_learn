import asyncio


async def fail_coro():
    await asyncio.sleep(1)
    raise ValueError("Вознникла ошибка в корутине fail_coro")


async def successful_coro():
    await asyncio.sleep(1)
    print("Корутина успешно завершена")


async def main():
    tasks = [asyncio.create_task(fail_coro()), asyncio.create_task(successful_coro())]

    try:
        await asyncio.gather(*tasks)

    except ValueError as e:
        print(f"Поймано исключение: {e}")

    for i, task in enumerate(tasks, 1):
        exc = task.exception()

        if exc:
            print(f"Задача {i} завершилась с исключением: {exc}")
        else:
            print(f"Задача {i} завершилась успешно")


if __name__ == "__main__":
    asyncio.run(main())
