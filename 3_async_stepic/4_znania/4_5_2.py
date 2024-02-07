import asyncio

async def task(lock):
    print("Задача приобретает блокировку")
    
    await lock.acquire()
    
    raise Exception("Ошибка и блокировка потеряна")

    print("Задача освобождает блокировку")
    lock.release()
        
        


async def main():
    lock = asyncio.Lock()
    
    asyncio.create_task(task(lock))
    await asyncio.sleep(1)
    print("Основная функция приобретает блокировку ....")
    await lock.acquire()
    
    lock.release()

    

if __name__ == "__main__":
    asyncio.run(main())