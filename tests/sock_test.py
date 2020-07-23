# import socket

# socket_family=socket.AF_INET
# socket_type=socket.SOCK_STREAM
# hostname = socket.gethostname()
# port=1234

# s = socket.socket (socket_family, socket_type, proto= 0)
# s.bind((hostname, port))


import socket

def Main():
   host = 'localhost'
   port = 8888
   serversocket = socket.socket()
   serversocket.bind((host,port))
   serversocket.listen(1)
   print('socket is listening')
   
   while True:
      conn,addr = serversocket.accept()
      print("Got connection from %s" % str(addr))
      msg = 'Connecting Established'+ "\r\n"
      conn.send(msg.encode('ascii'))
      conn.close()

if __name__ == '__main__':
   Main()