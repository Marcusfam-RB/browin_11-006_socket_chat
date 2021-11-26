import socket


host = 'localhost'
port = 5555

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind((host, port))

clients = {}
print('Server is running. Press ctrl+c to stop')
print('Listening for connections')

globe = ''
while True:
    print(clients)
    try:
        data, address = serversocket.recvfrom(1024)
        globe = address
        if address not in clients and len(clients.keys()) <= 100:
            clients[address] = None
            for client, client2 in clients.items():
                if client2 is None and client != address:
                    clients[client] = address
                    clients[address] = client
                    break

        if clients[address]:
            serversocket.sendto(data, clients[address])
    except:
        delete = clients[globe]
        clients[globe] = None
        clients.pop(delete)
