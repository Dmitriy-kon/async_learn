import asyncio

async def cook_dinner():
    print("Начинаем готовить обед")
    await asyncio.sleep(5)
    print("Обед готов")


async def do_laundry():
    print("Начинаем стирать одежду")
    await asyncio.sleep(3)
    print("Стирка завершена")

async def work_on_computer():
    print("Начинаем работать на компьютере")
    await asyncio.sleep(2)
    print("Работа с компьютером завершена")

async def main():
    dinner_task = asyncio.create_task(cook_dinner())
    laundry_task = asyncio.create_task(do_laundry())
    computer_task = asyncio.create_task(work_on_computer())

    await dinner_task
    await laundry_task
    await computer_task

asyncio.run(main())
