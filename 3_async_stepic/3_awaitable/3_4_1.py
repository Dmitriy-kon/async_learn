import asyncio


async def generate_message(number):
    print(f"Корутина generate с аргументом {number} запущена")
    await asyncio.sleep(number)
    print(f"Корутина generate с аргументом {number} завершена")
    

async def main():
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(generate_message(i)) for i in range(6, 0, -1)]

if __name__ == "__main__":
    asyncio.run(main())