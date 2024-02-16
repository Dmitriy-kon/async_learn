import asyncio


from data14 import banned_words2
import json


def get_data_from_json(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


async def check_message(message):
    message = message.lower()
    for word in banned_words2:
        if word in message:
            return word
    return False


async def get_message_by_role(message, role, ban_word):
    if role == "admin":
        return f"{role}: {message}"
    if role == "moderator":
        return f"{role}: {message.replace(ban_word, "****")}"
    if role == "student":
        return f"{role}: В сообщении есть запрещённое слово, сообщение скрыто"


async def get_message(data):
    _, message = data.get("message_id"), data.get("message")
    task = asyncio.current_task()

    role = task.get_name()

    if "Task" in role:
        print("None: ERROR_USER_NONE")
        return
    if role == "black_list_user":
        print(f"{role}: Пользователь забанен, сообщение скрыто")
        return

    ban_word = await check_message(message)
    if ban_word:
        message = await get_message_by_role(message, role, ban_word)
        print(message)
    else:
        print(f"{role}: {message}")


async def main():
    data = get_data_from_json("3_async_stepic/6_task/data_json_14_2.json")
    tasks = []

    for i in data:
        id, message, role = i.values()
        task = asyncio.create_task(
            get_message({"message_id": id, "message": message}), name=role
        )
        tasks.append(task)

    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        pass


if __name__ == "__main__":
    asyncio.run(main())
