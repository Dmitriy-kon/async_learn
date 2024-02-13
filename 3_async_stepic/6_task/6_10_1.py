import asyncio


async def print_hello():
    current_task = asyncio.current_task()
    current_loop = current_task.get_loop()
    print("Событийный цикл:",current_loop)

async def main():
    await asyncio.create_task(print_hello())

if __name__ == "__main__":
    asyncio.run(main())
