import os

def create_a_bridge_network_driver():
    confirm = input(f"use {create_a_bridge_network_driver.__name__} ?")
    if confirm == 'Y':
        os.system('docker network create -d bridge mybridge docker run -d --net mybridge --name db redis docker run -d --net mybridge -e DB=db -p 8000:5000 --name web chrch/web')

