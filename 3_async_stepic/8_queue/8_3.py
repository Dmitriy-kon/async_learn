import asyncio
import random


async def producer(queue):
    for i in range(5):
        item = f"Элемент {i}"
        await queue.put(item)
        print(f"producer добавил элемент {item} в очередь")


async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break

        print(f"Consumer получил из очереди элемент {item}")


async def main():
    queue = asyncio.Queue()

    prod_task = asyncio.create_task(producer(queue))
    cons_task = asyncio.create_task(consumer(queue))

    await prod_task
    await queue.put(None)
    await cons_task


if __name__ == "__main__":
    asyncio.run(main())
