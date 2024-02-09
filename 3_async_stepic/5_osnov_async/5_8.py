import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется {x} секунд")
    await asyncio.sleep(x)
    return x * 2

async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется {x} секунд")
    await asyncio.sleep(x)
    return x + 2

async def portal_operator(x):
    print("Оператор портала запущен")
    activate_energy =  await asyncio.create_task(activate_portal(x))
    
    if activate_energy > 4:
        perform_energy = await asyncio.create_task(perform_teleportation(1))
    else:
        perform_energy = await asyncio.create_task(perform_teleportation(activate_energy))
    
    print(f"Результат активации портала: {activate_energy} энергии")
    print(f"Результат телепортации: {perform_energy} энергии")


async def main():
    await portal_operator(1)    # await task1
    print("|", "-" * 23, "|")
    print("-" * 25)
    await portal_operator(3)    # await task1
    # await task1


if __name__ == "__main__":
    asyncio.run(main())
        
    
    
    
    
    