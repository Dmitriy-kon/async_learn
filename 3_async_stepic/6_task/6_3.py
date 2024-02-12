import asyncio


async def task_func():
    print("Task executed")
    await asyncio.sleep(1)
    print("Task finished")
    return "Task result from coro"


async def main():
    task = asyncio.create_task(task_func())
    print(f"первая проверка задачи - {task.done()}")
    print("Задача отправилась в цикл событий")
    print()
    await task
    print()
    print(f"последняя проверка задачи - {task.done()}")
    print(f"Результат задачи - {task.result()}")

if __name__ == "__main__":
    asyncio.run(main())
