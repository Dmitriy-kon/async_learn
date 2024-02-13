import asyncio
import aiohttp


async def download_file(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = response.headers.get("Content-Disposition", "")
            if filename:
                filename = filename.split("=")[1]
            else:
                raise ValueError("Invalid Content-Disposition header")

            task = asyncio.current_task()

            with open(filename, "wb") as f:
                while True:
                    chunk = await response.content.read(1024)



                    if not chunk:
                        break
                    f.write(chunk)
            task.set_name(f"Downloaded {filename}")


async def main():
    urls = [
        "https://www.example.com/file1.txt",
        "https://www.example.com/file2.txt",
        "https://www.example.com/file3.txt",
    ]
    tasks = [asyncio.create_task(download_file(url)) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
