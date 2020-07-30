import socket
import typing
import os
import colorama 
import time
colorama.init()
CF = colorama.Fore

class PopModePrime(object):
    def __init__(self):
        self.name = 'Pop-mode-Prime'

    def scan_all_wireless(self):
        print(CF.RESET)
        # time.sleep(1)
        os.system('nmcli -f ALL dev wifi')
     
        

    def get_local_ip(self) -> typing.Optional[str]:
        # Auto-Detect local IP. This is required as re-injecting to 127.0.0.1 does not work.
        # https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 80))
            print(s.getsockname()[0])
            return s.getsockname()[0]
        except OSError:
            print(CF.RED,"[!] ERROR")
            print(CF.RESET)
            return None
        finally:
            print("[:] END")
            s.close()
        

PopModePrime().scan_all_wireless()
    
        
        