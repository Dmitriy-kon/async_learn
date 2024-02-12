import asyncio
import websockets


async def client():
    async with websockets.connect("ws://localhost:8080") as websocket:
        await websocket.send("Hello, server")
        response = await websocket.recv()
        print(response)


async def main():
    await client()


if __name__ == '__main__':
    asyncio.run(main())
