import asyncio
from faker import Faker

faker = Faker()


class C:
    norm = "\33[0m"
    blue = "\33[94m"
    green = "\33[92m"
    red = "\33[31m"


users = [
    "sasha",
    "petya",
    "masha",
    "katya",
    "dima",
    "olya",
    "igor",
    "sveta",
    "nikita",
    "lena",
    "vova",
    "yana",
    "kolya",
    "anya",
    "roma",
    "nastya",
    "artem",
    "vera",
    "misha",
    "liza",
]

c = C()


def limit_rate(calls_limit: int = 5, timeout: int = 3):
    def wrapper(coro):
        semaphore = asyncio.Semaphore(calls_limit)

        async def inner_coro(*args, **kwargs):
            async with semaphore:
                await asyncio.sleep(timeout)
                return await coro(*args, **kwargs)

        return inner_coro

    return wrapper

count = 0

# @limit_rate(calls_limit=3, timeout=0)
# async def user_request(username: str):
#     global count
#     print(f"{c.green}Запрос пользователя {username} начался{c.norm}")
#     count += 1
#     await asyncio.sleep(1)
#     print(f"{c.red}Запрос пользователя {username} закончился{c.norm}")
#     print(f"Всего запросов: {count}")

async def user_request(semaphore: asyncio.Semaphore, username: str):
    global count
    # count = 0
    async with semaphore:
        print(f"{c.green}Запрос пользователя {username} начался{c.norm}")
        count += 1
        await asyncio.sleep(1)
        print(f"{c.red}Запрос пользователя {username} закончился{c.norm}")
        print(f"Всего запросов: {count}")


async def main():
    semaphore = asyncio.Semaphore(3)
    tasks = [asyncio.create_task(user_request(semaphore, username)) for username in users]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())