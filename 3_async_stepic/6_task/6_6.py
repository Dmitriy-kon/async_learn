import asyncio

async def task_coroutine(num):
    await asyncio.sleep(1)
    print(f"Задача {num} выполнена")


async def main():
    tasks = [asyncio.create_task(task_coroutine(i)) for i in range(5)]
    all_tasks = asyncio.all_tasks()

    print(f"Количество задач: {len(tasks)}")

    await asyncio.gather(*tasks)


    for task in all_tasks:
        print(f"Задача {task.get_name()} выполнена")

if __name__ == "__main__":
    asyncio.run(main())
