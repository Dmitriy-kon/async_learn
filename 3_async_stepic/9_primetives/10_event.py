import asyncio

event = asyncio.Event()

async def wait_for_event():
    print("Ждем события")
    await event.wait()
    print("Событие получено")

async def set_event():
    print("Событие установлено")
    event.set()

async def main():
    tasks = [asyncio.create_task(wait_for_event()) for i in range(5)]
    await asyncio.gather(*tasks, set_event())

asyncio.run(main())