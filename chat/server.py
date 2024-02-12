import socket, threading

UDP_MAX_SIZE = 65535*2

# server.listen()

flag = True


def listen(host: str= "localhost", port: int = 1111):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    print(f"Server started on {host}:{port}")
    
    members = []
    
    while True:
        # msg, adress = server.accept()
        msg, adress = server.recvfrom(UDP_MAX_SIZE)
        
        if adress not in members:
            members.append(adress)
        
        if not msg:
            continue
            
        client_id = adress[1]
        print(msg.decode("utf-8"))
        
        if msg.decode("utf-8") == "__join":
            print(f"Client {client_id} joined")
            continue
        
        # msg = f"client {client_id}: {msg.decode('utf-8')}"
        # msg = f"client {client_id}: {msg.decode('utf-8')}"
        for member in members:
            if member == adress:
                continue
            
            server.sendto(msg, member)

if __name__ == "__main__":
    listen()
        
        


# while flag:
#     msg = client.recv(1024).decode("utf-8")
#     if msg == "quit":
#         flag = False
#     else:
#         print(msg)
#     client.send(input("Server>>> ").encode("utf-8"))

# client.close()
# server.close()


#Coded by Yashraj Singh Chouhan
# import socket, threading                                                #Libraries import

# host = '127.0.0.1'                                                      #LocalHost
# port = 7976                                                             #Choosing unreserved port

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              #socket initialization
# server.bind((host, port))                                               #binding host and port to socket
# server.listen()

# clients = []
# nicknames = []

# def broadcast(message):                                                 #broadcast function declaration
#     for client in clients:
#         client.send(message)

# def handle(client):                                         
#     while True:
#         try:                                                            #recieving valid messages from client
#             message = client.recv(1024)
#             broadcast(message)
#         except:                                                         #removing clients
#             index = clients.index(client)
#             clients.remove(client)
#             client.close()
#             nickname = nicknames[index]
#             broadcast('{} left!'.format(nickname).encode('ascii'))
#             nicknames.remove(nickname)
#             break

# def receive():                                                          #accepting multiple clients
#     while True:
#         client, address = server.accept()
#         print("Connected with {}".format(str(address)))       
#         client.send('NICKNAME'.encode('ascii'))
#         nickname = client.recv(1024).decode('ascii')
#         nicknames.append(nickname)
#         clients.append(client)
#         print("Nickname is {}".format(nickname))
#         broadcast("{} joined!".format(nickname).encode('ascii'))
#         client.send('Connected to server!'.encode('ascii'))
#         thread = threading.Thread(target=handle, args=(client,))
#         thread.start()

# receive()