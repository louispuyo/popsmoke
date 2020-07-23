import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8888
while True:
    s.connect((host, port))
    msg = s.recv(1024)

    s.close()
    print (msg.decode('ascii'))