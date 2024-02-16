import asyncio


from data14 import banned_words
import json

def get_data_from_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

async def check_message(message):
    message = message.lower()
    return any(word in message for word in banned_words)


async def get_message(data):
    id, message = data.get("message_id"), data.get("message")

    if await check_message(message):
        task = asyncio.current_task()
        task.cancel()
        print(f"В сообщении {id} стоп слово: task.done(): {task.done()}")
    else:
        print(f"{id}: {message}")


async def main():
    data = get_data_from_json('3_async_stepic/6_task/data_json_14.json')
    tasks = [asyncio.create_task(get_message(message_info)) for message_info in data]

    # async with asyncio.TaskGroup() as tg:
    #         tasks = [tg.create_task(get_message(message_info)) for message_info in data]
    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        pass



    # for task in tasks:
    #     try:
    #         await task
    #     except asyncio.CancelledError:
    #         pass


if __name__ == "__main__":
    asyncio.run(main())
