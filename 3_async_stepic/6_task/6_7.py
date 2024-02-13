import asyncio

async def my_coro():
    print(f"Имя корунтины: {asyncio.current_task().get_name()}")
    asyncio.current_task().set_name("Новое название корунтины")
    print(f"Имя корунтины: {asyncio.current_task().get_name()}")

async def main():
    task = asyncio.create_task(my_coro(), name="Моя корунтина")
    # task.set_name("Корунтин")
    await task

if __name__ == "__main__":
    asyncio.run(main())
