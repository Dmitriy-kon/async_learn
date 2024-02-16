import asyncio

async def foo():
    await asyncio.sleep(1)
    for stack in asyncio.current_task().get_stack():
        print(stack)

async def main():
    # await asyncio.create_task(foo())
    await asyncio.gather(foo(), foo())

if __name__ == "__main__":
    asyncio.run(main())
