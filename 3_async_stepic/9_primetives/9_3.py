import asyncio


semaphore = asyncio.Semaphore(2)


async def my_coro(id):
    print(f"Корунтина {id} хочет получить семафор")
    async with semaphore:
        print(f"Корунтина {id} получил семафор")
        await asyncio.sleep(1)
    print(f"Корунтина {id} освободил семафор")


async def main():
    tasks = [asyncio.create_task(my_coro(i)) for i in range(5)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())