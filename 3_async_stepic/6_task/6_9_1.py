import asyncio


async def my_coro(seconds):
    print(f"Корунтина {asyncio.current_task().get_name()} запущена и будет выполняться {seconds} сек")

    try:
        await asyncio.sleep(seconds)
    except asyncio.CancelledError:
        print(f"Корунтина {asyncio.current_task().get_name()} была прервана")
        raise

    if asyncio.current_task().cancelling():
        print(f"Корутина {asyncio.current_task().get_name()} отменяется")

async def main():
    task_1 = asyncio.create_task(my_coro(5))
    task_2 = asyncio.create_task(my_coro(10))

    await asyncio.sleep(2)
    task_1.cancel()

    await asyncio.gather(task_1, task_2, return_exceptions=True)

    if task_1.cancelled():
        print(f"Корутина {asyncio.current_task().get_name()} отменена её флаг отмены {task_1.cancelled()}")

    if task_2.cancelled():
        print(f"Корутина {asyncio.current_task().get_name()} отменена её флаг отмены {task_2.cancelled()}")

if __name__ == "__main__":
    asyncio.run(main())
