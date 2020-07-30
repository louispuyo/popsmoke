import hashlib
from getpass import getpass
import colorama
from commands import autocomplete, pop_mode_prime
import readline

colorama.init()
CF = colorama.Fore

class WooPrimeClass(object):
    
    def __init__(self):
        self.access = False
        self.Label = \
            """
   ____            ____                  _        ____       _                
  |  _ \ ___  _ __/ ___| _ __ ___   ___ | | _____|  _ \ _ __(_)_ __ ___   ___ 
  | |_) / _ \| '_ \___ \| '_ ` _ \ / _ \| |/ / _ \ |_) | '__| | '_ ` _ \ / _ |
  |  __/ (_) | |_) |__) | | | | | | (_) |   <  __/  __/| |  | | | | | | |  __/
  |_|   \___/| .__/____/|_| |_| |_|\___/|_|\_\___|_|   |_|  |_|_| |_| |_|\___|
             |_|


            """

    def get_access(self):

        chaine_mot_de_passe = b"popsmoke-007"
        temp_pass_dev = b'pop'
        mot_de_passe_chiffre = hashlib.sha1(temp_pass_dev).hexdigest()

        verrouille = True
        while verrouille:
            entre = getpass("Tapez le mot de passe : ") # azerty
            # On encode la saisie pour avoir un type bytes
            entre = entre.encode()
            
            entre_chiffre = hashlib.sha1(entre).hexdigest()
            if entre_chiffre == mot_de_passe_chiffre:
                verrouille = False
            else:
                print("Mot de passe incorrect")
                self.access = False
                return self.access

        print("Mot de passe accepté...")
        self.access = True
        return self.access
    
    def WooPrimePortail(self):
        self.access = self.get_access()
        loop = 1
        poprime = pop_mode_prime.PopModePrime()
        function_prime_list = {"get_all_wireless    ":poprime.scan_all_wireless, "get_local_ip":poprime.get_local_ip}
            
        completer = autocomplete.MyCompleter(['pop-mode','get_all_wireless','super_hazer', 'get_local_ip'])
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')

        while self.access:
            if loop%100 == 1:
                print(CF.MAGENTA,self.Label)
                print(CF.RESET)
                for index,j in enumerate(function_prime_list.keys()):
                    print(f"{index} - {j}")
            for i in range(loop+1):
                loop+=1
                Input = input(f"\n[{i}][{i+7}]Prime> ")
                if Input == 'exit':
                    print(CF.LIGHTRED_EX, "EXITING POP SMOKE PRIME...\n\n")
                    self.access = False
                    break
                if Input in function_prime_list.keys():
                    print(CF.LIGHTGREEN_EX, "\n Processing... \n")
                    print(CF.RESET)
                    function_prime_list[Input]()
                    
                
                    
    

