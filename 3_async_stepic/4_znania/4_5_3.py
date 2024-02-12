import asyncio

async def task(number, lock1, lock2):
    print(f"Задача {number} приобретает блокировку 1")
    
    async with lock1:
        await asyncio.sleep(1)
        print(f"Задача {number} приобретает блокировку 2")
        
        async with lock2:
            pass
        
        


async def main():
    lock1 = asyncio.Lock()
    lock2 = asyncio.Lock()
    
    # В данном сегменте происходит deadlock
    coro1 = task(1, lock1, lock2)
    coro2 = task(2, lock2, lock1)
    
    await asyncio.gather(coro1, coro2)

    

if __name__ == "__main__":
    asyncio.run(main())