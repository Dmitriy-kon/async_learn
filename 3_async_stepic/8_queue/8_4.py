import asyncio

async def lifoqueue_example():
    lifo_queue = asyncio.LifoQueue(maxsize=3)
    
    await lifo_queue.put("Первая запись")
    await lifo_queue.put("Вторая запись")
    await lifo_queue.put("Третья запись")

    last_item = await lifo_queue.get()
    print(last_item)

    second_last_item = await lifo_queue.get()
    print(second_last_item)

    first_item = await lifo_queue.get()
    print(first_item)

async def main():
    await lifoqueue_example()

if __name__ == "__main__":
    asyncio.run(main())