import asyncio
import os

import aiofiles


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