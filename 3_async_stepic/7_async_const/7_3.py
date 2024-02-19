import asyncio
from aiofile import async_open


async def read_file_line_by_line(file_path):
    async with async_open(file_path, 'r') as f:
        async for line in f:
            print(line.strip("\n"))

async def append_to_file(file_path, text):
    async with async_open(file_path, 'a') as f:
        await f.write(text)

async def main():
    file_path = r'D:\python\asyncio\3_async_stepic\7_async_const\7_2.py'
    await read_file_line_by_line(file_path)
    await append_to_file(file_path, '# Hello, from aiofile!\n')
    await read_file_line_by_line(file_path)
    
if __name__ == '__main__':
    asyncio.run(main())


