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
    print(f"{c.green}worker {num} запустился{c.norm}")
    await asyncio.sleep(num)
    
    print(f"{c.green}worker {num} закончил работу{c.norm}")
    await barrier.wait()
    print(f"{c.red}worker {num} прошел барьер{c.norm}")

async def main():
    barrier = asyncio.Barrier(3)
    
    tasks = [asyncio.create_task(worker(barrier, i)) for i in range(20)]
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
        
    