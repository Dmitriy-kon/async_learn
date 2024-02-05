import asyncio
from random import randint


async def waiter(condition: asyncio.Condition, id: int):
    async with condition:
        print(f"Waiter {id} is awaiting")
        # Вводим корунтины в режим ожидания
        await condition.wait()

        num = randint(1, 5)
        print(f"Waiter {id} generated {num}")


async def starter(condition: asyncio.Condition):
    print("Starter is sleeping 5 seconds")
    await asyncio.sleep(5)

    async with condition:
        # будим только 2 корунтины
        condition.notify(2)

        # Уведомляем все корунтины, что пора работать
        # condition.notify_all()


async def main():
    condition = asyncio.Condition()

    waiters = [
        asyncio.create_task(waiter(condition, i))
        for i in range(5)
    ]

    await asyncio.gather(*waiters, starter(condition))


asyncio.run(main())
