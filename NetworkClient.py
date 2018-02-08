import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 1201
BUFFER_SIZE = 4028
MESSAGE = "Hello, World!"
byteMessage= bytearray()
byteMessage.extend(map(ord, MESSAGE))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print('Connected')
s.send(byteMessage)
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)
