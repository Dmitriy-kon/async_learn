import asyncio
from faker import Faker

faker = Faker()

class C:
    norm = "\33[0m"
    blue = "\33[94m"
    green = "\33[92m"
    red = "\33[31m"


c = C()

async def worker(barrier: asyncio.Barrier, num):
    print(f"{c.green}worker {num} начал свою работу и ждет барьера{c.norm}")
    await barrier.wait()
    await asyncio.sleep(0.5)
    print(f"{c.red}worker {num} прошел барьер{c.norm}")
    
async def main():
    barrier = asyncio.Barrier(3)    
    tasks = [asyncio.create_task(worker(barrier, i)) for i in range(5)]
    
    
    print(f"{c.blue}Ждем пока worker's пройдут барьер{c.norm}")
    await barrier.wait()
    
    await asyncio.gather(*tasks)
    print(f"{c.red}Все worker's прошли барьер{c.norm}")
    # for task in tasks:
        # task.cancel()

if __name__ == "__main__":
    asyncio.run(main())