import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            return data

async def process_data(data):
    print(f"Received data: {data[:50]}")
    # Может включать в себя любую другую логику, которую вы хотите выполнить с полученными данными,
    # например, сохранение в базу данных, отправку уведомлений или обновление интерфейса пользователя.

async def long_polling(url):
    while True:
        await asyncio.sleep(5)
        data = await fetch_data(url)
        if data:
            await process_data(data)

async def main():
    task = asyncio.create_task(long_polling("https://example.com/api/data"))
    await task
    
if __name__ == "__main__":
    asyncio.run(main())