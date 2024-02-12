import asyncio


async def foo():
    print("Запущена корунтина foo")
    await asyncio.sleep(5)
    raise Exception("ОШИБКА В foo")
    print("Переключение контекста в foo")
    

async def bar():
    print("Запущена корунтина bar")
    await asyncio.sleep(3)
    raise Exception("ОШИБКА В foo")
    
    print("Переключение контекста в bar")


async def main():
    tasks = [asyncio.create_task(foo()), asyncio.create_task(bar())]
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    
    for task in done:
        print(f"Завершено {task}")
        if task.exception() is not None:
            print(f"ОШИБКА: {task.exception()}")
    
    for task in pending:
        print(f"Задача в ожидании: {task}")
        
if __name__ == "__main__":
    asyncio.run(main())