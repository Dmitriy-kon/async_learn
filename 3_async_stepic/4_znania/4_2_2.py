import asyncio


async def access_resource_lock(resource, lock):
    # await lock.acquire()

    # try:
    #     print(f"Доступ получен {resource}")
    #     await asyncio.sleep(2)
    #     print(f"Доступ закрыт {resource}")
    # finally:
    #     print("-" * 25)
    #     lock.release()
    async with lock:
        print(f"Доступ получен {resource}")
        await asyncio.sleep(2)
        print(f"Доступ закрыт {resource}")

        print("-" * 25)


async def access_resource(resource):
    print(f"Доступ получен {resource}")
    await asyncio.sleep(2)
    print(f"Доступ закрыт {resource}")
    print("-" * 25)


async def main():
    lock = asyncio.Lock()
    resource = "--Защищенный ресурс--"

    tasks = [access_resource_lock(f"{resource}{i}", lock) for i in range(1, 6)]
    # tasks = [access_resource(f"{resource}{i}") for i in range(1, 6)]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
