import asyncio

users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']

class C:
    norm = "\33[0m"
    blue = "\33[94m"
    green = "\33[92m"
    red = "\33[31m"


c = C()

async def user_connection(name: str, condition: asyncio.Condition):
    async with condition:
        print(f"{c.blue}Пользователь {name} ожидает доступ к базе данных{c.norm}")
        await condition.wait()
        print(f"{c.red}Пользователь {name} подключился к базе данных{c.norm}")
    await asyncio.sleep(0.5)
    print(f"{c.red}Пользователь {name} отключился от базы данных{c.norm}")

async def controller_db(condition: asyncio.Condition, n):
    # for _ in range(n):
    while True:
        await asyncio.sleep(2)
        async with condition:
            condition.notify(3)

async def main():
    condition = asyncio.Condition()
    tasks_users = [asyncio.create_task(user_connection(user, condition)) for user in users]
    controller_task = asyncio.create_task(controller_db(condition, n=len(tasks_users)))
    
    # await asyncio.gather(*tasks_users, controller_task)
    await asyncio.gather(*tasks_users)

if __name__ == "__main__":
    asyncio.run(main())