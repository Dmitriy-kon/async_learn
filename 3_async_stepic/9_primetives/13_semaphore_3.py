import asyncio
from faker import Faker

faker = Faker()


class C:
    norm = "\33[0m"
    blue = "\33[94m"
    green = "\33[92m"
    red = "\33[31m"


c = C()

sem1 = asyncio.Semaphore(2)
sem2 = asyncio.Semaphore(2)


async def task_s(id: int):
    async with sem1, sem2:
        print(f"{c.green}Задача {id} начала выполнение{c.norm}")
        await asyncio.sleep(1)
        print(f"{c.red}Задача {id} закончила выполнение{c.norm}")

async def main():
    tasks = [asyncio.create_task(task_s(i)) for i in range(10)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())