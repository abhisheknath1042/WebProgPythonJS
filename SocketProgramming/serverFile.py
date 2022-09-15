import socket

s = socket.socket()

print('Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print("Waiting for Connections.....")

while True:
    clientSocket, addressClient = s.accept()
    name = clientSocket.recv(1024).decode()
    print("Connected with: ", addressClient, name)
    clientSocket.send(bytes('Welcome to Abssyz', 'utf-8'))
    clientSocket.close()
