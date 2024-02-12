import asyncio

async def my_coroutine():
    print("my_coroutine started")

    await asyncio.sleep(2)

    print("my_coroutine finished")
    return 42

async def main():
    task = asyncio.create_task(my_coroutine())
    await asyncio.sleep(1)
    print("Main продолжает работу")
    await task

    print(f"Результат выполнение корунтины my_coroutine - {task.result()}")

if __name__ == "__main__":
    asyncio.run(main())
