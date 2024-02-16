import asyncio


async def important_task():
    print("Важная задача")
    await asyncio.sleep(4)
    print("Важная задача завершена")
    return "Важная задача"
    try:
        await asyncio.shield(asyncio.sleep(5))

    except asyncio.CancelledError:
        print("Важная задача отменена")

    print("Задача завершена")

async def main():
    task = asyncio.create_task(important_task())
    await asyncio.sleep(2)
    # asyncio.shield(task).cancel()
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Задача отменена")

    else:
        print("Задача успешно завершена")

if __name__ == "__main__":
    asyncio.run(main())
