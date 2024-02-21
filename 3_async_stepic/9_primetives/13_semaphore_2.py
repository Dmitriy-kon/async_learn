import asyncio
from random import random
from faker import Faker

faker = Faker()


class C:
    norm = "\33[0m"
    blue = "\33[94m"
    green = "\33[92m"
    red = "\33[31m"


c = C()



def limit_rate(calls_limit: int =5, timeout: int =3):
    def wrapper(coro):
        semaphore = asyncio.Semaphore(calls_limit)
        
        async def inner_coro(*args, **kwargs):
            async with semaphore:
                await asyncio.sleep(timeout)
                return await coro(*args, **kwargs)
        return inner_coro
    return wrapper
            

async def some_task(semaphore: asyncio.Semaphore, number: int):
    async with semaphore:
        
        value = random()
        await asyncio.sleep(value)
        print(f"{c.green}Задача {number} получила {value}{c.norm}")

async def some_task2(semaphore: asyncio.Semaphore, number: int):
    async with semaphore:
        await asyncio.sleep(0.5)
        print(f"{c.green}Задача {number} начала выполнение{c.norm}")
        await asyncio.sleep(1)
        print(f"{c.red}Задача {number} закончила выполнение{c.norm}")

async def main():
    semaphore = asyncio.Semaphore(5)
    # tasks = [asyncio.create_task(some_task(semaphore, i)) for i in range(10)]
    tasks2 = [asyncio.create_task(some_task2(semaphore, i)) for i in range(50)]
    # await asyncio.wait(tasks)
    await asyncio.gather(*tasks2)

if __name__ == "__main__":
    asyncio.run(main())