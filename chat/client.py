import socket, threading

UDP_MAX_SIZE = 65535*2


def listen(server: socket.socket):
    while True:
        msg = server.recv(UDP_MAX_SIZE)
        print(msg.decode("utf-8").split()[-1])


def connect(host: str = "localhost", port: int = 1111):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server.connect((host, port))
    name = input("Your name is: ")
    
    threading.Thread(target=listen, args=(server,)).start()
    
    while True:
        msg = input(f"{name}==> ")
        # msg = input()
        server.send(f"{name}==>\t{msg}".encode('utf-8'))


if __name__ == "__main__":
    print("Client welcome")
    connect()
    

# import socket, threading
# nickname = input("Choose your nickname: ")

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket initialization
# client.connect(('127.0.0.1', 7976))                             #connecting client to server

# def receive():
#     while True:                                                 #making valid connection
#         try:
#             message = client.recv(1024).decode('ascii')
#             if message == 'NICKNAME':
#                 client.send(nickname.encode('ascii'))
#             else:
#                 print(message)
#         except:                                                 #case on wrong ip/port details
#             print("An error occured!")
#             client.close()
#             break
# def write():
#     while True:                                                 #message layout
#         message = '{}: {}'.format(nickname, input(''))
#         client.send(message.encode('ascii'))

# receive_thread = threading.Thread(target=receive)               #receiving multiple messages
# receive_thread.start()
# write_thread = threading.Thread(target=write)                   #sending messages 
# write_thread.start()