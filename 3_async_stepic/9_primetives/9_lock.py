import asyncio


lock = asyncio.Lock()

async def my_task(task_id):
    print(f"Задача {task_id} ожидает блокировки с помощью Block")
    
    
    async with lock:
        print(f"Задача {task_id} получила блокировку")
        await asyncio.sleep(2)
    print(f"Задача {task_id} освободила блокировку")
    
    # await lock.acquire()
    
    # try:
    #     print(f"Задача {task_id} получила блокировку")
    #     await asyncio.sleep(2)
    # finally:
    #     print(f"Задача {task_id} освободила блокировку")
    #     lock.release()

async def main():
    tasks = [asyncio.create_task(my_task(i)) for i in range(5)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())