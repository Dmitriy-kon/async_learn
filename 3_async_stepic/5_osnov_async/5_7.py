import asyncio

async def task_func():
    print("Task executed")
    await asyncio.sleep(3)
    return "Task result from coro"

async def main():
    task = asyncio.create_task(task_func())
    finished, pending = await asyncio.wait({task}, timeout=2)
    # assert not pending, f"{len(pending)} pending task"
    print(f"Pending: {pending}")
    for i in pending:
        res = await i
    print(f"Task result: {res}")
    # print(f"Task result: {task.result()}")
    
if __name__ == "__main__":
    asyncio.run(main())