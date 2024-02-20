import asyncio

condiotion = asyncio.Condition()


async def consumer(condiotion: asyncio.Condition):
    async with condiotion:
        print("consumer: ждет условия")
        await condiotion.wait()
        print("consumer: условие выполнено")


async def producer(condiotion: asyncio.Condition):
    print("producer: ожидает")
    await asyncio.sleep(1)
    print("producer: просыпается и устанавливает условие")
    async with condiotion:
        condiotion.notify_all()

async def main():
    tasks = [asyncio.create_task(consumer(condiotion)) for _ in range(5)]
    await asyncio.gather(*tasks, asyncio.create_task(producer(condiotion)))
    
    # await producer(condiotion)

asyncio.run(main())