import asyncio

async def print_message():
    while True:
        print("Имитация работы функции")
        await asyncio.sleep(1)

async def interrupt_handler(interupt_flag):
    while True:
        await asyncio.sleep(0.5)
        
        # if interupt_flag.is_set():
        await interupt_flag.wait()
        print("Программа остановлена")
        interupt_flag.clear()
        break

async def main():
    interrupt_flag = asyncio.Event()
    
    task1 = asyncio.create_task(print_message())
    task2 = asyncio.create_task(interrupt_handler(interrupt_flag))
    
    while True:
        await asyncio.sleep(3)
        
        interrupt_flag.set()
        await task2
        task2 = asyncio.create_task(interrupt_handler(interrupt_flag))

if __name__ == "__main__":
    asyncio.run(main())
        