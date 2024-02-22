import asyncio
import aiofiles



async def read_from_file():
    async with aiofiles.open('file.txt', mode='r+') as f:
        async for line in f:
            print(line, end='')
        await f.write('Hello from aiofiles\n')

async def main():
    await read_from_file()

if __name__ == '__main__':
    asyncio.run(main())