import asyncio
import websockets


async def server(websocket, path):
    async for message in websocket:
        print(message)
        await websocket.send(message)


async def main():
    await websockets.serve(server, "localhost", 8080)


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())
    # asyncio.get_event_loop().run_until_complete(websockets.serve(server, "localhost", 8080))
    asyncio.get_event_loop().run_forever()
