import asyncio
from random import randint


class C:
    norm = '\33[0m'
    blue = '\33[94m'
    green = '\33[92m'


c = C()


async def producer(queue, name):
    timeout = randint(1, 5)
    await queue.put(timeout)
    print(f"{c.blue}Producer {name} положил {timeout} в очередь {queue}{c.norm}")


async def consumer(queue, name="main"):
    while True:
        timeout = await queue.get()
        await asyncio.sleep(timeout)
        print(f"{c.green}Consumer {name} ate {timeout} из очереди {queue}{c.norm}")
        queue.task_done()


async def main():
    queue = asyncio.Queue(maxsize=3)
    producers = []

    for i in range(12):
        task = asyncio.create_task(producer(queue, name=i))
        producers.append(task)

    consumers = []
    for i in range(4):
        task = asyncio.create_task(consumer(queue, str(i)))
        consumers.append(task)

    await asyncio.gather(*producers)
    await queue.join()

    for c in consumers:
        c.cancel()


asyncio.run(main())
