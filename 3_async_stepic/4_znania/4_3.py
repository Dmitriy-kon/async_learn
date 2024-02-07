import asyncio

shared_resource = 0

async def update_resource(lock: asyncio.Lock = None, name=""):
    global shared_resource
    
    if lock:
        async with lock:
            print("Начинаем обновление shared_resource")
            temp = shared_resource
            await asyncio.sleep(2)
            shared_resource = temp + 1
            print("Обновлен shared_resource завершено")
    else:
    
        print("Начинаем обновление shared_resource")
    
        temp = shared_resource
        await asyncio.sleep(2)  

        shared_resource = temp + 1
        print("Обновлен shared_resource завершено")


async def main():
    lock = asyncio.Lock()
    await asyncio.gather(*[update_resource() for _ in range(5)])
    # await asyncio.gather(update_resource(lock), update_resource(lock))
    print(f"shared_resource: {shared_resource}")

if __name__ == "__main__":
    asyncio.run(main())