import asyncio



class C:
    norm = "\33[0m"
    blue = "\33[94m"
    green = "\33[92m"
    red = "\33[31m"


c = C()


async def worker(numbers, event: asyncio.Event):
    for i in numbers:
        if i == 15:
            event.set()

        print(f"{c.blue}Поиск события: Обрабатываемое число {i}{c.norm}")

        await asyncio.sleep(0.3)


async def manager(event):
    print(f"{c.red}Ожидаем событие")
    await event.wait()
    print(f"{c.red}Событие получено")

async def main():
    number = range(1, 30)
    event = asyncio.Event()
    
    await asyncio.gather(worker(number, event), manager(event))

if __name__ == "__main__":
    asyncio.run(main())