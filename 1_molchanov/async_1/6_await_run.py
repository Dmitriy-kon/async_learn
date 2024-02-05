import asyncio


async def coro(message):
    print(message)
    await asyncio.sleep(1)
    print(message)


async def main():
    print("-- main начало работы")

    asyncio.create_task(coro("Абсолютно уникальный текст"))

    # print(asyncio.all_tasks())
    await asyncio.sleep(1)

    print("-- main работа окончена")


asyncio.run(main())
