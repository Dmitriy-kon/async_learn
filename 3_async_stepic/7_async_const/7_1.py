import asyncio
import random


async def async_gen():
    for i in range(5):
        await asyncio.sleep(random.randint(1, 3))
        yield i

async def main():
    async for i in async_gen():
        print(i)

asyncio.run(main())