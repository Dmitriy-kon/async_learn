import asyncio
import random


async def task_func(task_id):
    print(f"Старт задачи {task_id}, из корунтины task_func")
    await asyncio.sleep(random.randint(1, 3))
    print(f"Задача {task_id} завершена")


async def main():
    tasks = []
    # lock = asyncio.Lock()
    for i in range(5):
        task = asyncio.create_task(task_func(i))

        tasks.append(task)
    print("Задачи созданы")

    loop = 1

    while len(tasks) > 0:
        # async with lock:
        print(f"Это луп {loop}")
        loop = loop + 1
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

        for task in done:
            print(f"Задача выполнена - {task.get_name()} и имеет флаг {task.done()}")


if __name__ == "__main__":
    asyncio.run(main())
