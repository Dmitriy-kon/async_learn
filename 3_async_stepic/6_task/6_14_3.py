import asyncio
import itertools
import random

SHAPES = ["circle", "star", "square", "diamond", "heart"]
COLORS = ["red", "blue", "green", "yellow", "purple"]
ASCTIONS = ["change_color", "explode", "disappear"]

combinations = list(itertools.product(SHAPES, COLORS, ASCTIONS))

async def firework_launch(color, shape, action):
    await asyncio.sleep(random.randint(1, 2))
    
    print(f"Запущен {color} {shape}, салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")



async def main():
    # tasks = []
    # for shape, color, action in combinations:
    #     task = asyncio.create_task(firework_launch(color, shape, action))
    #     tasks.append(task)
    
    async with asyncio.TaskGroup() as tg:
        for shape, color, action in combinations:
            tg.create_task(firework_launch(color, shape, action))
    
    # tasks = [asyncio.create_task(firework_launch(color, shape, action)) for shape, color, action in combinations]
    # await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
    
    
