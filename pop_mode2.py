import os
import time
import colorama
import readline
from commands import autocomplete
from docker import Pocker
colorama.init()
CF = colorama.Fore


def p_active(init=False):
    if not init:
        print(CF.GREEN, "PopHide mode activated ...")
        time.sleep(0.4)
        print('\n\n------------------------------\n')
        print(CF.YELLOW, "Waiting For verification ...")
        # identity = input('identifiant : ')
        time.sleep(0.3)
        print('\n\n\n')
        print("DEV.0.12 - BETA version - DEBUGER ACTIVE -")
        time.sleep(0.3)
        message = """ 
                              ______  __  __  ___  _  _______ 
     _ __   ___  _ __       / / ___||  \/  |/ _ \| |/ / ____|
    | '_ \ / _ \| '_ \     / /\___ \| |\/| | | | | ' /|  _|  
    | |_) | (_) | |_) |   / /  ___) | |  | | |_| | . \| |___ 
    | .__/ \___/| .__/___/_/  |____/|_|  |_|\___/|_|\_\_____|
    |_|         |_| |_____|  
        """
        print(CF.WHITE, message)


    cmdList = {'pile':pile, 'Docker_SIDE':Docker_SIDE, }
    completer = autocomplete.MyCompleter(cmdList.keys())
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')

    while True:
        print(CF.RESET)
        enter = input("?> ")
        if enter == 'exit':
            os.sys.exit()
        if enter in cmdList.keys():
            cmdList[enter]()
        



def pile():
    try:
        flag = os.sys.argv[1]

        if flag == '-d':
            print(CF.GREEN, "developement mode activate")
        else:
            print(CF.RESET, "prod\n")
    except:
        pass

    os.system('ls -1')
    return p_active(init=True)

def fastapi(api_name="api", port=7007, host='0.0.0.0', swagger_urlpath=None):
    os.system('mkdir app && cd app \
        touch api.py')
    base = "from fastapi import FastAPI\nfrom uvicorn import run\n\n# API #\napi = FastAPI()\n\n@api.get(\"/\")\ndef root():\n   return {\"hello\":\"world\"}"
    print(base)
    
    os.system(f"cd app && echo '{base}' > api.py")


def FastApi():
    with open ('Popsmoke/pop_mode.py','r') as f:
        content = f.read()
        print(content)


def Docker_SIDE():
    func_list = {"create_a_bridgeNet":Pocker.create_a_bridge_network_driver}
    return func_list


