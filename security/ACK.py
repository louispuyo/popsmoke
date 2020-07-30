from scapy.all import *
from scapy.layers.can import *
import colorama

colorama.init()

class COLORS(colorama.ansi.AnsiFore):
    def __init__(self):
        color = colorama.Fore
        self.CYAN = color.CYAN
        self.GREEN = color.GREEN
        self.LIGHTBLACK_EX = color.LIGHTBLACK_EX
        self.MAGENTA = color.MAGENTA
        self.RED = color.RED
        self.RESET = color.RESET
        self.LIGHTMAGENTA_EX = color.LIGHTMAGENTA_EX
        self.LIGHTYELLOW_EX = color.LIGHTYELLOW_EX
 

class Mechant(object):
    def __init__(self):
        pass

    def trace_route(self):
        example = 'www.google.com'
        hostname = input(f'hostname (ex:{example}) : ')
        if hostname == '':
            hostname = example
        for i in range(1,28):
            pkt = IPField(hostname, default=1), UDPDrain(port=33434)

            reply = sr1(pkt, verbose=0)
            if reply is None:
                break
            elif reply.type == 3:
                print(COLORS().GREEN, 'Done !')
                break
            else:
                print(f"{i} hope away : ", reply.scr)


class _CAN(object):

    def __init__(self):
        pass

    def Send_p(self):
        load_layer('can')
        conf.contribs['CANSocket'] = {'use-python-can' : True}
        load_contrib('cansocket')
        from can.interfaces.vector import VectorBus

        socket = CANSocket(iface=VectorBus(0, bitrate=1000000))
        packet = CAN(identifier=0x123, data=b'01020304')

        socket.send(packet)
        rx_packet = socket.recv()

        socket.sr1(packet)

    def create_frame(self):
        frame = CAN(identifier=0x200, length=8, data=b'\x01\x02\x03\x04\x05\x06\x07\x08')
        return frame.show()

    def explore_inet6(self):
        return explore(scapy.layers.inet6)

    class HTTP(object):
        
        def __init__(self):
            from scapy.layers.http import HTTPRequest, HTTPResponse
            self.HTTPRequest = HTTPRequest
            self.HTTPResponse = HTTPResponse

        def http_request_show(self):
            return self.HTTPRequest().show()
        
        def http_response_show(self):
            return self.HTTPResponse().show()

    

class SOCKET(object):

    pass


class Mail(object):
    def __init__(self):
        pass 

    @property
    def send_email(self):
        self._email = email
        return self._email
    

    #TO FINISH
    @send_email.getter
    def send_email(self):
        email = input("email destination : ")
    
        return email
        


# _CAN().HTTP().http_response_show()


# ==================== MIXINS ===========


import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = f"{cur_thread.name}: {data}"
        self.request.sendall(f"{response}".encode('utf-8'))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print(f"Received: {response}")
    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    client(ip, port, b"Hello World 1")
    client(ip, port, b"Hello World 2")
    client(ip, port, b"Hello World 3")
    
    client(ip, port, bytes(input("message : "), encoding='utf-8'))
    while True:
          client(ip, port, bytes(input("message : "), encoding='utf-8'))

    

    server.shutdown()
    server.server_close()