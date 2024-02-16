import asyncio

async def async_operation(num):
    print(f"Выполняется асинхронная операция {num}")
    await asyncio.sleep(2)
    print(f"Завершена асинхронная операция {num}")
    return "Результат асинхронной операции"

def on_completion(task: asyncio.Task):
    res = task.get_name()
    result = task.result()
    print(f"Callback функция вызвана {res}. Результат - {result}")

async def main():
    task = asyncio.create_task(async_operation(1))
    task.add_done_callback(on_completion)

    task2 = asyncio.create_task(async_operation(2))
    task2.add_done_callback(on_completion)
    task2.remove_done_callback(on_completion)
    await task
    await task2

if __name__ == "__main__":
    asyncio.run(main())
