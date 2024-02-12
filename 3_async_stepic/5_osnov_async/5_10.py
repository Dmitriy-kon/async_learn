import asyncio
import threading


async def task1(id, loop):
    print(f"Task {id} started, loop = {loop}")
    await asyncio.sleep(2)
    print(f"Task {id} finished")


async def task2(id, loop: asyncio.AbstractEventLoop):
    print(f"Task {id} started, loop = {loop}")
    await asyncio.sleep(3)
    print(f"Task {id} finished")

def start_loop(loop, coro):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coro)

async def main():
    loop1 = asyncio.new_event_loop()
    loop2 = asyncio.new_event_loop()
    
    coro1 = task1(1, loop1)
    coro2 = task2(2, loop2)
    
    thread1 = threading.Thread(target=start_loop, args=(loop1, coro1))
    thread2 = threading.Thread(target=start_loop, args=(loop2, coro2))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    asyncio.run(main())