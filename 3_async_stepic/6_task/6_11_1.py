import asyncio

async def inner_func():
    print("Выполняется внутренняя функция")
    task = asyncio.current_task()
    task.print_stack()
    print("-"*25)
    print("Завершена внутренняя функция")
    print("-"*25)


async def middle_func():
    print("Выполняется middle функция")
    await inner_func()
    task = asyncio.current_task()
    task.print_stack()
    print("-"*25)
    print("Завершена middle функция")
    print("-"*25)


async def outer_func():
    print("Выполняется outer функция")
    await middle_func()
    task = asyncio.current_task()
    task.print_stack()
    print("-"*25)
    print("Завершена outer функция")
    print("-"*25)


async def main():
    await outer_func()

if __name__ == "__main__":
    asyncio.run(main())
