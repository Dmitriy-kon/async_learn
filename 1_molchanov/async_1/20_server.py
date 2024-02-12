import asyncio

from fastapi import FastAPI

app = FastAPI(title="Asyncio test")
lock = asyncio.Lock()
count = 0


@app.get("/")
async def main():
    global count

    async with lock:
        count += 1

    return {"message": f"Hello world",
            "count": count}


@app.get("/hello")
async def hello(name: str):
    return {"message": f"Hello {name}",
            "count": count}
