import asyncio


bank_account = 1000


async def withdraw_money(amout, lock):
    global bank_account
    
    async with lock:
    
        if bank_account >= amout:
            print(f"Снятие {amout} средств успешно")
            
            await asyncio.sleep(1)
            bank_account -= amout

async def main():
    lock = asyncio.Lock()
    tasks = [asyncio.create_task(withdraw_money(800, lock)) for _ in range(2)]
    
    await asyncio.gather(*tasks)
    print(bank_account)
        
if __name__ == "__main__":
    asyncio.run(main())