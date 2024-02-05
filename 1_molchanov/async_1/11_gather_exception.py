import asyncio

import asyncio
import aiohttp


class WriteToFIle:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file_object = open(self.filename, 'w')
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_object:
            self.file_object.close()


class AsyncSession:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()


async def check(url):
    async with AsyncSession(url) as response:
        html = await response.text()
        return f"{url=}: {html[:40]}\n"


async def coro_norm():
    return "Hello world"


async def coro_value_error():
    raise ValueError


async def coro_type_error():
    raise TypeError


async def main():
    try:
        results = await asyncio.gather(
            coro_norm(),
            coro_type_error(),
            coro_value_error(),
            return_exceptions=True,
        )
        print(results)

    except ValueError as e:
        print(f"Вышла ошибка {e=}")
    except TypeError as e:
        print(f"Вышла ошибка {e=}")

    # except* ValueError as e:
    #     for i in e.exceptions:
    #         print(f"Вышла ошибка {i=}")
    # except* TypeError as e:
    #     for i in e.exceptions:
    #         print(f"Вышла ошибка {i=}")

    #
    # async with asyncio.TaskGroup() as tg:
    #     print(type(tg))
    #     print(dir(tg))
    #
    #     res1 = tg.create_task(check("https://facebook.com"))
    #     res2 = tg.create_task(check("https://youtube.com"))
    #     res3 = tg.create_task(check("https://google.com"))
    #
    # print(res1.result())
    # print(res2.result())
    # print(res3.result())


asyncio.run(main())
