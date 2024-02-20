import asyncio

async def producer(queue):
    for i in range(5):
        await queue.put(i)
        print(f"Producer: {i} добавлен в очередь {queue}")
        await asyncio.sleep(1)


async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        
        print(f"Consumer: {item} извлечен из очереди {queue}")
        await asyncio.sleep(0.5)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    # task_prod = asyncio.create_task(producer(queue))
    task_consum = asyncio.create_task(consumer(queue))

    async with asyncio.TaskGroup() as tg:
        tg.create_task(producer(queue))
        
    await queue.join()
        
    
    # await asyncio.gather(task_prod)
    
    # task_consum.cancel()
if __name__ == "__main__":
    asyncio.run(main())