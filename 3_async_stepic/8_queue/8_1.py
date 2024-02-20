import asyncio
import random


async def producer(queue: asyncio.Queue):
    print("Запуск производителя")
    for i in range(10):
        value = random.random()
        await asyncio.sleep(value)
        await queue.put(value)
    await queue.put(None)
    print("Производитель: Done")


async def consumer(queue):
    print("Потребитель: Запущен")
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Потребитель: {item:.2f}")
        # queue.task_done()
    print("Потребитель: Done")


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))


if __name__ == "__main__":
    asyncio.run(main())
