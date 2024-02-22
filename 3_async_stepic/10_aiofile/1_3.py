import asyncio
import aiofiles

from concurrent.futures import ThreadPoolExecutor


class C:
    norm = "\33[0m"
    blue = "\33[94m"
    green = "\33[92m"
    red = "\33[31m"


c = C()

fd = os.open('file.txt', os.O_RDONLY)


async def read_from_desk():
    async with aiofiles.open(fd, mode='r+', closefd=False) as f:
        content = await f.read()
    return content

async def main():
    res = await read_from_desk()
    os.close(fd)
    print(res)

if __name__ == '__main__':
    asyncio.run(main())