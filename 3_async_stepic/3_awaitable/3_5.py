import asyncio



async def coro_number(number):
    print(f"Коронтина под номером {number} начата")
    await asyncio.sleep(1)
    print(f"Коронтина под номером {number} завершена")

async def main():
    tasks = [
        asyncio.create_task(coro_number(i))
        for i in range(1, 10)
    ]
    for i in tasks:
        await i
    # res = await asyncio.gather(*tasks)
    

if __name__ == "__main__":
    asyncio.run(main())