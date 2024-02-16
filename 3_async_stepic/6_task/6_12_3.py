import asyncio

from data_6_12 import codes, messages

data = {code: message for code, message in zip(codes, messages)}
# data2 = {message: code for code, message in zip(codes, messages)}


async def get_message(code):
    message = data[code]
    # print(f"Сообщение: {message}")
    task = asyncio.current_task()

    # if message in data2:
    task.add_done_callback(print_code)
    # print(f"Код: {code}")
    code_check = int(code[-1], 16)
    if code_check % 2 == 0:
        return code, "Неверный код, сообщение скрыто"

    return code, message

def print_code(task: asyncio.Task):
    code, message = task.result()
    print(f"Сообщение: {message}")
    print(f"Код: {code}")

async def main():
    tasks = [asyncio.create_task(get_message(code)) for code in data]
    await asyncio.gather(*tasks)
    # for task in tasks:
    # tasks = [get_message(message) for message in messages]
    # for task in tasks:
        # task.add_done_callback(print_code)
        # await task

if __name__ == "__main__":
    asyncio.run(main())
