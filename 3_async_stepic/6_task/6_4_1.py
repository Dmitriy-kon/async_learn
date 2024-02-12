import asyncio


async def my_coroutine():
    print("my_coroutine started")
    await asyncio.sleep(4)
    print("my_coroutine finished")
    return 42

async def main():
    task = asyncio.create_task(my_coroutine())

    await asyncio.sleep(1)
    print("Main продолжает работу")

    try:
        await asyncio.wait_for(task, timeout=1)
        res = task.result()
        print(f"Результат выполнение корунтины my_coroutine - {res}")

    except asyncio.TimeoutError:
        print(f"Задача {task.get_name()} не было завершена в уканное время")

if __name__ == "__main__":
    asyncio.run(main())
