import asyncio


balance = 100

lock = asyncio.Lock()


async def deposit(amount):
    global balance

    async with lock:
        print(f"Баланс поплнен на {amount} кредитов")
        balance += amount
        print(f"Текущий баланс {balance}")


async def withdraw(amount):
    global balance

    async with lock:
        if balance >= amount:
            print(f"Баланс снимается на {amount} кредитов")
            balance -= amount
            print(f"Текущий баланс {balance}")
        else:
            print(
                f"Попытка снять {amount}, недостаточно средств, текущий баланс {balance} кредитов"
            )


async def main():
    task1 = asyncio.create_task(deposit(300))
    task2 = asyncio.create_task(withdraw(500))
    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    asyncio.run(main())
