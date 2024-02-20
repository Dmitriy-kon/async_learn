import asyncio

async def task(name, priority, queue):
    await queue.put((priority, name))
    print(f"Задача {name} добавлена в очередь с приоритетом {priority}")

async def main():
    quque = asyncio.PriorityQueue()
    await task("task_1", 4, quque)
    await task("task_2", 2, quque)
    await task("task_3", 3, quque)
    await task("task_4", 1, quque)
    
    while not quque.empty():
        prioriy, name = await quque.get()
        print(f"{name}, с приоритетом {prioriy}")

if __name__ == "__main__":
    asyncio.run(main())