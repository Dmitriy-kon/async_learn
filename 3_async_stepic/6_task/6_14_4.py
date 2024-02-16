import asyncio


from bus_passangers import passengers


class Passanger:
    def __init__(self, Name, Age, Speed, Job):
        self.name = Name
        self.age = Age
        self.speed = Speed
        self.job = Job

    def __repr__(self) -> str:
        return f"Passange({self.name}, {self.age}, {self.speed}, {self.job})"


passengers = [Passanger(**passenger) for passenger in passengers]


async def take_bus(passanger: Passanger):
    await asyncio.sleep(passanger.speed)
    # print(f"{passanger.name} took a bus")
    return passanger


async def main():
    tasks = [asyncio.create_task(take_bus(passanger), name=passanger) for passanger in passengers]
    # tasks = [take_bus(passanger) for passanger in passengers]
    
    # try:
    #     await asyncio.wait_for(asyncio.gather(*tasks), timeout=5)
    # except asyncio.TimeoutError:
    #     # print("В автобусе нет пассажиров")
    #     pass
    
    # for task in tasks:
    #     if not task.cancelled():
    #         res = task.result()
    #         print(f"{res.name} сел в автобус")
    #     else:
    #         # res = task.get_name()
    #         print(f"{task.get_name()} не успел вовремя сесть в автобус")

    
    
    
    fin, pend = await asyncio.wait(tasks, timeout=5)
    for task in fin:
        res = task.result()
        print(f"{res.name} сел в автобус")

    for task in pend:
        print(task.done())
        print(task.cancelled())
        passenger = task.get_coro().cr_frame.f_locals["passanger"]
        print(f"{passenger.name} {passenger.job} не успел вовремя сесть в автобус")


if __name__ == "__main__":
    asyncio.run(main())
