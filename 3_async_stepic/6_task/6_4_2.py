import asyncio
import random


async def my_coroutine(n):
    print(f"my_coroutine {n} started")
    sleep_time = random.randint(1, 10)
    await asyncio.sleep(sleep_time)
    print(f"my_coroutine {n} finished, after {sleep_time}")
    return sleep_time

async def main():
    tasks = [asyncio.create_task(my_coroutine(i)) for i in range(5)]

    await asyncio.sleep(1)
    print("Main продолжает работу")
    timeout_list = [random.randint(1, 3) for i in range(5)]

    for i, task in enumerate(tasks):
        try:
            await asyncio.wait_for(task, timeout=timeout_list[i])
            res = task.result()
            print(f"Результат выполнения корунтины my_coroutine {i} - {res}")
        except asyncio.TimeoutError:
            print(f"Задача {task.get_name()} не было завершена в уканное время (таймаут: {timeout_list[i]}) сек..")

if __name__ == "__main__":
    asyncio.run(main())
