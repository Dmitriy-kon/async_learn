import asyncio

async def worker(name, lifo_queue):
    while True:
        task = await lifo_queue.get()
        
        print(f"Рабочий_{name}. Получил задачу: {task}")
        await asyncio.sleep(0.5)
        lifo_queue.task_done()

async def main():
    lifo_queue = asyncio.LifoQueue()
    for i in range(10):
        await lifo_queue.put(i)
    
    workers = [
        asyncio.create_task(worker(f"Рабочий_{i}", lifo_queue))
        for i in range(3)
    ]
    await lifo_queue.join()
    for w in workers:
        w.cancel()

if __name__ == "__main__":
    asyncio.run(main())