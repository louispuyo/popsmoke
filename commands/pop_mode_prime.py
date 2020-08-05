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
        self.functions = ['pop-mode','get_all_wireless','super_hazer', 'get_local_ip', 'run_a_container', 'kill_all_container', 'attach_container_to_the_last','create_a_network', 
        'Docker_swarm', 'tcpdump', 'tcpdumpall', 'tcpdumpraw', 'commands', 'tcpdumpshark']
        self.Label = \
            """
   ____            ____                  _        ____       _                
  |  _ \ ___  _ __/ ___| _ __ ___   ___ | | _____|  _ \ _ __(_)_ __ ___   ___ 
  | |_) / _ \| '_ \___ \| '_ ` _ \ / _ \| |/ / _ \ |_) | '__| | '_ ` _ \ / _ |
  |  __/ (_) | |_) |__) | | | | | | (_) |   <  __/  __/| |  | | | | | | |  __/
  |_|   \___/| .__/____/|_| |_| |_|\___/|_|\_\___|_|   |_|  |_|_| |_| |_|\___|
             |_|


            """

    
    def commands(self):
        print(CF.LIGHTMAGENTA_EX, self.Label)
        print(CF.RESET, "\n")
        for index, command in enumerate(self.functions):
            print(index, " - ", command)

        print("\n\n")
    
    def tcpdumpraw(self):
        number = input('how many packet want you to send ? ')
        os.system('sudo tcpdump --list-interfaces')
        interface = input('choose interface (optinal) : ')
        if interface == '':
            os.system(f'sudo tcpdump -n -c {number}')
        else:
            os.system(f'sudo tcpdump -n -i {interface} -c {number}')
    
    def tcpdumpall(self):
        verbose = input('do you want verbose mode ? ')
        number = input('how many packet want you to send ? ')
        # save = input('do you want to save it in a file') -w option did it 
        if verbose in ['yes','y','Y','YES','Yes']:
            level = input('choose a level between [1-3] :')
            level = (level if level != '' else 1)
            print(CF.GREEN, f"\n[i] verbose mode enabled at level {level}\n")
            print(CF.RESET)
            verb_level = "v"*int(level)
            os.system(f'sudo tcpdump -A -{verb_level} -c {number}')
        else:
            os.system(f'sudo tcpdump -A -c {number}')

    def tcpdump(self):
        os.system('sudo tcpdump --list-interfaces')
        interface = input('choose interface (optinal) : ')
        number = input('how many packet want you to send ? ')
        if interface == '':
            os.system(f'sudo tcpdump -c {number}')
        else:
            os.system(f'sudo tcpdump -i {interface} -c {number}')
        
    
    def tcpdumpshark(self):
        os.system('sudo tcpdump --list-interfaces')
        interface = input('choose interface (optinal) : ')
        number = input('how many packet want you to send ? ')
        if interface == '':
            os.system(f'sudo tcpdump -c {number}')
        else:
            os.system(f'sudo tcpdump -i {interface} -c {number} -XX')
        

    def scan_all_wireless(self):
        print(CF.RESET)
        # time.sleep(1)
        return os.system('airport -s')
    
    def create_wireless_interface(self):
        wname = input('interface name: ')
        os.system(f'airodump-ng {wname}')
    
    def Kill_all_container(self):
        os.system('docker kill $(docker ps -q)')
    
    def Create_a_network(self):
        name = input('name of the network: ')
        os.system(f'docker network create {name}')

    def Docker_swarm(self):
        # docker network create mynet --driver overlay
        # docker service create --network mynet myimage
        NotImplementedError
    
    def Create_container_on_another_Network(self):
        network = input('name of the network: ')
        key_word = input('key word: ')
        os.system(f'docker run -d --name {network}-{key_word}-1 --net-alias {key_word} --net {network} elasticsearch:2')

    def attach_container_to_the_last(self):
        os.system('docker attach $(docker ps -lq)')
    
    def start_redis_container(self):
        network = input('network name: ')
        os.system(f'docker run --net {network} --net-alias redis -d redis')
    
    def run_and_make_reacheable_from_a_network(self):
        docker_name = input('dockerName: ')
        network = input('network: ')
        bridge = int(input('position: '))
        os.system(f'docker run -d --name {docker_name} --net {network} elasticsearch:{bridge}')

    def run_a_container(self):
        os.system('docker ps -q')
        print('\n')
        container_name = input('container_name: ')
        command = f'docker run -ti {container_name}'
        os.system(command)
    
    def history_of_container(self):
        pass

    def build_an_image(self):
        image_tag = input('image_tag: ')
        version = input('version ? : ')
        os.system(f'docker build --tag {image_tag}:{version}')
    
    def run_mykali_admin(self):
        network = input('network : ')
        os.system('docker run -it --net="{network}" --privileged --name aircrack mykali bash')



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
    
        
        