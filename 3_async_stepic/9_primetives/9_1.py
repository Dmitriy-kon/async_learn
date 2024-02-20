import asyncio


lock = asyncio.Lock()

async def my_coro(id):
    print(f"Корунтина {id} хочет получить блокировку")
    
    async with lock:
        print("*"*25)
        print(f"Корунтина {id} получил блокировку")
        await asyncio.sleep(1)
        print(f"Корунтина {id} освободил блокировку")
        print("*"*25)

async def main():
    tasks = [asyncio.create_task(my_coro(i)) for i in range(5)]
    await asyncio.gather(*tasks)
    
if __name__ == "__main__":
    asyncio.run(main())