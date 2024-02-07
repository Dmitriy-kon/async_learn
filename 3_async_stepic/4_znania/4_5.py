import asyncio

async def task(lock):
    print("Задача пытается перехватить замок....")
    
    async with lock:
        print("Задача вновь пытается перехватить замок")
        
        async with lock:
            print("Ошибка")
            pass

async def main():
    lock = asyncio.Lock()
    await task(lock)
    

if __name__ == "__main__":
    asyncio.run(main())