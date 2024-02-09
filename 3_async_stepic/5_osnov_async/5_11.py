import asyncio


async def my_task(idx):
    print(f"Task {idx} started")
    await asyncio.sleep(1)
    print(f"Task {idx} finished")


async def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    tasks = [asyncio.create_task(my_task(i)) for i in range(1, 6)]
    await asyncio.gather(*tasks)
    
    
    loop.close()


if __name__ == "__main__":
    asyncio.run(main())