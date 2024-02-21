import asyncio



class C:
    norm = "\33[0m"
    blue = "\33[94m"
    green = "\33[92m"
    red = "\33[31m"


c = C()


async def worker(condition: asyncio.Condition, msg):
    async with condition:
        print(f"{c.blue}worker() получил блокировку, сообщение {msg}{c.norm}")
        await condition.wait()
        await asyncio.sleep(0.8)
        print(f"{c.blue}worker() сработало событие и продолжается работа{c.norm}")
        print(f"{c.blue}worker() разблокирован,сообщение {msg}{c.norm}")

async def starter(condition: asyncio.Condition):    
    await asyncio.sleep(1)
    
    async with condition:
        print(f"{c.red}starter() получил блокировку{c.norm}")
        print(f"{c.red}starter() логика окончена{c.norm}")
        
        condition.notify_all()

async def main():
    condition = asyncio.Condition()
    tasks = [asyncio.create_task(worker(condition, f"Messege is {i}")) for i in range(5)]
    task_start = asyncio.create_task(starter(condition))
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())