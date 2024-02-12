import asyncio
import aiohttp


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.headers

async def main():
    tasks = [fetch_data('https://yandex.ru/') for _ in range(10)]
    results = await asyncio.gather(*tasks)
    print(*[f"{res}" for res in results], sep='\n')

if __name__ == '__main__':
    asyncio.run(main())