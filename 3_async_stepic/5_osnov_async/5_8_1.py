import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется {x} секунд")
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется {x} секунд")
    await asyncio.sleep(x)
    return x + 2


async def recharg_portal(x):
    print(f"Подзарядка портала в процессе, требуется {x} секунд")
    await asyncio.sleep(x)
    return x * 3

async def check_portal_stability(x):
    print(f"Проверка портала в процессе, требуется {x} секунд")
    await asyncio.sleep(x)
    return x + 4

async def restore_portal(x):
    print(f"Восстановление портала в процессе, требуется {x} секунд")
    await asyncio.sleep(x)
    return x * 5

async def close_portal(x):
    print(f"Закрытие портала в процессе, требуется {x} секунд")
    await asyncio.sleep(x)
    return x - 1


async def portal_operator(x=1):
    act_res = await activate_portal(3)
    per_res = await perform_teleportation(2)
    print()
    
    async with asyncio.TaskGroup() as tg:
        rech_portal =  tg.create_task(recharg_portal(2))
        check_portal = tg.create_task(check_portal_stability(2))
        rest_portal = tg.create_task(restore_portal(3))
    
    print()
    close_res = await close_portal(5)
    
    print("*"*25)
    print(f"Результат активации портала: {act_res} энергии")
    print(f"Результат телепортации: {per_res} энергии")
    print(f"Результат подзарядки портала: {rech_portal.result()} энергии")
    print(f"Результат проверки портала: {check_portal.result()} энергии")
    print(f"Результат восстановления портала: {rest_portal.result()} энергии")
    print(f"Результат закрытия портала: {close_res} энергии")
    print("*"*25)
    
    



async def main():
    await portal_operator()  # await task1


if __name__ == "__main__":
    asyncio.run(main())
