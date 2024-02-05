import asyncio

from faker import Faker

faker = Faker('en_Us')


async def get_user(n=1):
    await asyncio.sleep(0.2)
    for i in range(n):
        name, surname = faker.name_male().split()
        yield name, surname


async def main():
    l = [name async for name in get_user(3)]
    s = {name async for name in get_user(3)}
    d = {name: surname async for name, surname in get_user(3)}

    print(s)


asyncio.run(main())
