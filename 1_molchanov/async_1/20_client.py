import asyncio
import time

import aiohttp

lock = asyncio.Lock()


async def make_request(url, lock_=False):
    async with aiohttp.ClientSession() as session:
        if lock_:
            async with lock:
                async with session.get(url) as response:
                    data = await response.json()
                    print(data)

                    await asyncio.sleep(0.1)
        else:

            async with session.get(url) as response:
                data = await response.json()
                print(data)

                await asyncio.sleep(0.1)


async def get_data(url):
    await make_request(url)


async def get_data_lock(url):
    await make_request(url, True)


async def main():
    start = time.perf_counter()
    tasks = [
        asyncio.create_task(get_data('http://localhost:8000'))
        for _ in range(20)
    ]

    hello_tasks = [
        asyncio.create_task(get_data_lock(f'http://localhost:8000/hello/?name=Dima'))
        for _ in range(3)
    ]

    await asyncio.gather(*tasks, *hello_tasks)

    print(time.perf_counter() - start)


asyncio.run(main())
