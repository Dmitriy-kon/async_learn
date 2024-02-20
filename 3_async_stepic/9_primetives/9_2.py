import asyncio


event = asyncio.Event()


async def waiter():
    print("waiter: ожидает событие")
    await event.wait()
    print("waiter: событие обработано")

async def setter():
    print("setter: засыпает")
    x = 0
    while x < 5:
        print(f"setter: {x}")
        x += 1
        await asyncio.sleep(0.2)
    print("Setter: результат выполнения {x}")
    print("setter: проснулся и создал событие")
    event.set()

async def main():
    tasks = [asyncio.create_task(waiter()), asyncio.create_task(setter())]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())