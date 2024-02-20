import asyncio
import random


async def read_queue(queue):
    while True:
        item = await queue.get()

        print(f"Получен элемент из очереди: {item}")

async def main():
    queue = asyncio.Queue()
    task = asyncio.create_task(read_queue(queue))
    
    await queue.put("Первый элемент")
    await queue.put("Второй элемент")

if __name__ == "__main__":
    asyncio.run(main())