import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 1201
BUFFER_SIZE = 4028

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

done = False

conn, addr = s.accept()
print ('Connection address:', addr)

while not(done):
    byteData = conn.recv(BUFFER_SIZE)
    data = byteData.decode("utf-8")
    #if not data: break
    print ("received data:", data)
    conn.send(byteData)  # echo

conn.close()
