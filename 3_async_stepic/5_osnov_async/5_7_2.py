import asyncio

async def task_func(task_id):
    print(f"Task {task_id} executed")
    return f"Task {task_id} result from coro"

async def main():
    task = [asyncio.create_task(task_func(i)) for i in range(10)]
    
    _, pending = await asyncio.wait(task, timeout=2)
    assert not pending, f"{len(pending)} pending task"
    
    for i in task:
        print(f"Task {i.get_coro()} result: {i.result()}")
    # print(f"Task result: {task.result()}")
    
if __name__ == "__main__":
    asyncio.run(main())