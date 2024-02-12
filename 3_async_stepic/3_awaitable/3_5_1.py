import asyncio

max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0
}

class Counter:
    def __init__(self, max_counts: int, name: str, delay: int | float):
        self.max_counts = max_counts
        self.count = 0
        self.name = name
        self.delay = delay
            

    async def counter(self):
        while self.count < self.max_counts:
            await asyncio.sleep(self.delay)
            self.count += 1
            print(f"{self.name}: {self.count:.2f}")




async def main():
    counter1 = Counter(10, "Counter 1", 1)
    counter2 = Counter(5, "Counter 2", 2)
    counter3 = Counter(3, "Counter 3", 0.5)
    
    await asyncio.gather(counter1.counter(), counter2.counter(), counter3.counter())    


if __name__ == "__main__":
    asyncio.run(main())