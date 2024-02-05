import asyncio

from concurrent.futures import ProcessPoolExecutor

import aiohttp

from bs4 import BeautifulSoup


async def make_request(url, session: aiohttp.ClientSession):
    response = await session.get(url)

    if response.ok:
        return response
    else:
        print(f"{url} return: {response.status}")


async def get_image_page(queue: asyncio.Queue, session: aiohttp.ClientSession):
    url = "https://c.xkcd.com/random/comic/"
    response = await make_request(url, session)
    await queue.put(response.url)


def _parse_link(html):
    soup = BeautifulSoup(html, 'lxml')
    image_link = 'https:' + soup.select_one('div#comic>img').get('src')
    return image_link


async def get_image_url(pages_queue: asyncio.Queue, image_urls_queue: asyncio.Queue, session: aiohttp.ClientSession):
    while True:
        url = await pages_queue.get()
        response = await make_request(url, session)

        html = await response.text()

        # Получаем нынешний событийный цикл
        loop = asyncio.get_running_loop()
        # Создаем новый поток для сихроной функции
        with ProcessPoolExecutor() as pool:
            image_link = await loop.run_in_executor(
                pool, _parse_link, html
            )

        await image_urls_queue.put(image_link)

        pages_queue.task_done()


async def main():
    session = aiohttp.ClientSession()
    pages_queue = asyncio.Queue()
    image_urls_queue = asyncio.Queue()

    page_getters = []

    for i in range(4):
        task = asyncio.create_task(
            get_image_page(pages_queue, session)
        )
        page_getters.append(task)

    url_getters = []

    for i in range(4):
        task = asyncio.create_task(
            get_image_url(pages_queue, image_urls_queue, session)
        )
        url_getters.append(task)

    await asyncio.gather(*page_getters)

    await pages_queue.join()
    for task in page_getters:
        task.cancel()

    print(pages_queue)

    await session.close()


asyncio.run(main())
# asyncio.get_event_loop().run_until_complete(main())
