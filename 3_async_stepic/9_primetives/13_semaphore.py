import asyncio
from faker import Faker

faker = Faker()

users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']
users.extend([faker.name() for _ in range(10)])

class C:
    norm = "\33[0m"
    blue = "\33[94m"
    green = "\33[92m"
    red = "\33[31m"


c = C()

semaphore = asyncio.Semaphore(3)


def limit_rate(calls_limit: int =5, timeout: int =3):
    def wrapper(coro):
        semaphore = asyncio.Semaphore(calls_limit)
        
        async def inner_coro(*args, **kwargs):
            async with semaphore:
                res = await coro(*args, **kwargs)
                await asyncio.sleep(timeout)
                return res
        return inner_coro
    return wrapper
            

@limit_rate(calls_limit=2, timeout=3)
async def write_to_file(text):
    # async with semaphore:
        # await asyncio.sleep(0.5)
    print(f"{c.green}Запись в файл {text}{c.norm}", end="")
    with open("file.txt", 'a') as file:
        file.write(text)
        # await asyncio.sleep(5)

async def main():
    tasks = [asyncio.create_task(write_to_file(f"{user}\n")) for user in users]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())