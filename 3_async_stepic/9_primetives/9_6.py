import asyncio

async def worker(barrier: asyncio.Barrier, worker_num: int):
    print(f"Работник {worker_num} начал свою работу")
    await asyncio.sleep(1)
    print(f"Работник {worker_num} закончил свою работу и ожидает остальных")
    await barrier.wait()
    print(f"Все работники закончили. Работник {worker_num} продолжет свою работу")
    

async def main():
    barrier = asyncio.Barrier(3)
    tasks = [asyncio.create_task(worker(barrier, i)) for i in range(3)]
    await asyncio.gather(*tasks)
    
if __name__ == "__main__":
    asyncio.run(main())