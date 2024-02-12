import asyncio

def callback(future):
    print(f"Обратный вызов: результат асинхронной операции равен {future.result()}")

async def do_some_work(x):
    print(f"Выполнение работы: {x}")
    await asyncio.sleep(x)
    return x * 2

async def main():
    task = asyncio.create_task(do_some_work(2))
    task.add_done_callback(callback)
    await task

if __name__ == "__main__":
    asyncio.run(main())