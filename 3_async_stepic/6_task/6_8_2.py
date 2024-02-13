import asyncio

async def process_item(item):
    if item == 13 or item == "i":
        try:
            raise ValueError(f"Обработка исключения: {item}")
        except ValueError as e:
            print(f"{e}")
    print(f"Обработан элемент: {item}")
    return item

async def process_list(items):
    tasks = [asyncio.create_task(process_item(item)) for item in items]
    for task in tasks:
        try:
            await task
        except ValueError as e:
            task.set_exception(ValueError(f"Установлено исключение: {e}"))
            print(e)

async def main():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "i"]
    await process_list(items)

if __name__ == "__main__":
    asyncio.run(main())
