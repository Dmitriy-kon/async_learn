import asyncio
import aiohttp


async def async_url_generator(urls):
    for url in urls:
        yield url


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = [
        "https://google.com/",
        "https://github.com/",
        "https://python.org/",
    ]
    async with aiohttp.ClientSession() as session:
        async for url in async_url_generator(urls):
            res = await fetch(session, url)
            print(res[:50])


if __name__ == "__main__":
    asyncio.run(main())
# Hello, from aiofile!# Hello, from aiofile!# Hello, from aiofile!
# Hello, from aiofile!
# Hello, from aiofile!
# Hello, from aiofile!
# Hello, from aiofile!
