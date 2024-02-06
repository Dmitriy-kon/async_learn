import asyncio

async def producer():
    future = asyncio.Future()
    await asyncio.sleep(2)
    future.set_result("Futures is done")
    return future


async def consumer():
    future = await producer()
    print(await future)
    
    
if __name__ == "__main__":
    asyncio.run(consumer())