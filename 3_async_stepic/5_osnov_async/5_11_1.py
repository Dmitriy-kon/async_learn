import asyncio

async def task_1(idx):
    print(f"Task {idx} started")
    await asyncio.sleep(1)
    print(f"Task {idx} finished")

async def task_2(idx):
    print(f"Task {idx} started")
    await asyncio.sleep(1)
    print(f"Task {idx} finished")


async def main_1():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    tasks = [asyncio.create_task(task_1(i)) for i in range(1, 4)]
    await asyncio.gather(*tasks)
    print("-" * 25)
    print("Main_1 finished")
    print("-" * 25)
    loop.close()

async def main_2():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    tasks = [asyncio.create_task(task_2(i)) for i in range(1, 4)]
    await asyncio.gather(*tasks)
    print("-" * 25)
    print("Main_2 finished")
    print("-" * 25)
    loop.close()

async def main():
    await main_1()
    await main_2()

if __name__ == "__main__":
    asyncio.run(main())