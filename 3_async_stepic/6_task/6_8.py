import asyncio

async def raise_exception():
    raise RuntimeError("--Установлено исключение--")


async def main():
    task = asyncio.create_task(raise_exception())
    await asyncio.sleep(1)

    try:
        await task
    except Exception as e:
        print(f"Поймано исключение: {e}")

    exception = task.exception()

    if exception:
        print(f"Обработка исключения: {exception}")


if __name__ == "__main__":
    asyncio.run(main())
