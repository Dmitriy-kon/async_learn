import asyncio
import random

event = asyncio.Event()

async def number_generator():
    # event.is_set()
    
    lst = (random.randint(0, 100) for i in range(5000))
    
    for en, i in enumerate(lst):
        await asyncio.sleep(random.uniform(0, 0.1))
        
        if i == 33:
            event.set()
        
        print(f"Генерируем число : {i}")
        
        if event.is_set():
            print(f"Событие сработало. Завершаем цикл. Число {i} найдено за {en} попыток")
            break

async def main():
    await number_generator()
    
if __name__ == "__main__":
    asyncio.run(main())