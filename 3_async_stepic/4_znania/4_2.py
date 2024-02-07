import asyncio
import random
import aiohttp


async def process_data(data):
    print(f"Received data: {data}")


async def polling_network_device():
    while True:
        data = random.randint(1, 100)
        await process_data(data)
        
        await asyncio.sleep(5)
        
async def main():
    task = asyncio.create_task(polling_network_device())
    await task
    
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Программа остановлена")