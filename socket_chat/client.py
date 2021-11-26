import socket
import threading


def receive():
    while True:
        data = clientsocket.recv(1024)
        print(data.decode('utf-8'))


host = '127.0.0.1'
port = 5555


nickname = input("Введите ваш ник: ")
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.connect((host, port))
clientsocket.sendto(("В вашу комнату зашёл " + nickname).encode('utf-8'), (host, port))

thread = threading.Thread(target=receive)
thread.start()

while True:
    message = input()
    if not message:
        break
    clientsocket.sendto(('[' + nickname + ']: ' + message).encode('utf-8'), (host, port))

clientsocket.close()
