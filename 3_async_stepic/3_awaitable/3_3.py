import asyncio
from functools import wraps
import random
import time


def timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = await func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"Время выполнения: {end:.4f} секунд")
        return res

    return wrapper


class Pizzeria:
    def __init__(self, name):
        self.name = name

    async def make_pizza(self, order_id):
        cook_time = random.randint(
            2, 5
        )  # случайное время готовки пиццы от 2 до 5 секунд
        print(f"Пиццерия {self.name} начала готовить пиццу для заказа {order_id}.")
        await asyncio.sleep(cook_time)  # ожидание пока пицца готовится
        print(f"Пиццерия {self.name} закончила готовить пиццу для заказа{order_id}.")


@timer
async def make_pizza_gather(pizzeria, _range):
    tasks = [pizzeria.make_pizza(i) for i in _range]
    await asyncio.gather(*tasks)


@timer
async def make_pizza_task_group(pizzeria, _range):
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(pizzeria.make_pizza(i)) for i in _range]


async def main():
    pizzeria = Pizzeria("Тесто & Сыр")
    _range = range(1, 6)
    
    await make_pizza_gather(pizzeria, _range)
    print("Gather end")
    print()
    await make_pizza_task_group(pizzeria, _range)
    print("Task group end")
    # запуск всех задач (заказов)


if __name__ == "__main__":
    asyncio.run(main())
