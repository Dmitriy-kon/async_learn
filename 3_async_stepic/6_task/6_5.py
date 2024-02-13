import asyncio
from typing import Any


async def my_task(number):
    current_task: asyncio.Task[Any] | None = asyncio.current_task()
    print(
        f"Задача {number}, стартовала. Текущий объект задачи {current_task.get_name()}"
    )
    await asyncio.sleep(1)

    print("-" * 50)
    print(
        f"Задача {number}, завершена. Текущий объект задачи {current_task.get_name()}"
    )


async def main():
    task1 = asyncio.create_task(my_task(1))
    task2 = asyncio.create_task(my_task(2))

    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    asyncio.run(main())
