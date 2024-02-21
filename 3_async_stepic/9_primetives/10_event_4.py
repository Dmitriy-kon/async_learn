import asyncio



class C:
    norm = "\33[0m"
    blue = "\33[94m"
    green = "\33[92m"
    red = "\33[31m"


c = C()


ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]

async def sensor_worker(event: asyncio.Event, ip, id):
    print(f"{c.blue}Датчик {id} IP-адрес {ip} настроен и ожидает срабатывания{c.norm}")
    await event.wait()
    print(f"{c.red}Датчик {id} IP-адрес {ip} активирован, \"Wee-wee-wee-wee\"{c.norm}")


async def alarm(event: asyncio.Event):
    await asyncio.sleep(5)
    print(f"{c.red}Датчики зафиксировани движение")
    event.set()

async def main():
    event = asyncio.Event()
    tasks = [asyncio.create_task(sensor_worker(event, ip[i], i)) for i in range(5)]
    task_alarm = asyncio.create_task(alarm(event))
    
    await asyncio.gather(*tasks, task_alarm)

if __name__ == "__main__":
    asyncio.run(main())