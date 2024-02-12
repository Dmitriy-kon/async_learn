import asyncio


async def cook_dish(n):
    print(f"Повар {n} начинает готовить") # Повар n начинает готовить
    await asyncio.sleep(n) # Повар готовит блюдо n секунд.
    print(f"Повар {n} закончил готовить") # Повар n закончил готовить
    return f"Блюдо от повара {n}" # Возвращает строку, указывающую, что


async def main():
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(cook_dish(n)) for n in range(1, 6)]
    print([f"result: {res.result()}, {res.get_name()}" for res in tasks])
    exit()
    
    
    tasks = [asyncio.create_task(cook_dish(n)) for n in range(1, 6)]
    print(await asyncio.gather(*tasks))
    

if __name__ == "__main__":
    asyncio.run(main())