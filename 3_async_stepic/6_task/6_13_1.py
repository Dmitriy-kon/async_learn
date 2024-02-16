import asyncio
import aiohttp


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        "https://google.com/",
        "https://github.com/",
        "https://python.org/",
        "https://yandex.reu/",
    ]
    tasks = []

    for url in urls:
        task = asyncio.create_task(fetch(url))
        # tasks.append(asyncio.shield(task))
        tasks.append(task)

    responses = await asyncio.gather(*tasks, return_exceptions=True)

    for response in responses:
        if isinstance(response, Exception):
            print(f"Error: {response!r}")
        else:
            print(f"Успешный ответ{response[:50]}")

if __name__ == "__main__":
    asyncio.run(main())
