import asyncio



lock = asyncio.Lock()

robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']
count = 1

async def send_robot_to_point(name):
    global count
    async with lock:
        robot_id = asyncio.current_task().get_name()
        print(f"Робот {name}({robot_id}) отправляется в месту A")
        await asyncio.sleep(1)
        print(f"Робот {name}({robot_id}) достиг места А. Место А посещено {count} раз")
        count += 1 

async def main():
    tasks = [asyncio.create_task(send_robot_to_point(name), name=idx) for idx, name in enumerate(robot_names)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())