import asyncio
import socket


shared_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lock = asyncio.Lock()

async def read_socket():
    global shared_socket
    
    async with lock:    
    # Читем данные из сокета
        data = shared_socket.recv(1024) 
        print(f"Полученные данные: {data.decode()}")
    

async def write_socket(message):
    global shared_socket
    
    async with lock:
    # Отправляем данные в сокет
        shared_socket.send(message.encode())
        print(f"Сообщение {message} отправлено")


async def establish_connection():
    global shared_socket
    
    # Соединяемся с сервером
    shared_socket.connect(('localhost', 8888))
    print("Соединение установлено")
    task1 = asyncio.create_task(read_socket())
    task2 = asyncio.create_task(write_socket("Hello"))
    
    await asyncio.gather(task1, task2)
    
    shared_socket.close()
    
if __name__ == "__main__":
    asyncio.run(establish_connection())