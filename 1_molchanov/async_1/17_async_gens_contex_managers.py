import asyncio
from contextlib import contextmanager, asynccontextmanager

from redis import asyncio as aioredis


# Все что до yield декоратор использует в __enter__
# Все что после используется для __exit__
@contextmanager
def custom_open(filename, mode='w'):
    file_object = open(filename, mode)
    yield file_object
    file_object.close()


with custom_open('file.txt') as file:
    file.write("hello world")


@asynccontextmanager
async def redis_connection():
    try:
        redis = await aioredis.from_url("redis://localhost")
        yield redis
    finally:
        await redis.close()


async def main():
    async with redis_connection() as redis:
        # await redis.delete('a')
        await redis.set("a", "Hello world")
        await redis.set("b", "Some keys")
        res = await redis.get("a")
        print(res)


asyncio.run(main())