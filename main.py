"""
this is not module stupid pylint
"""
import os
import sys
import json
def normalize(inp):
    """
    standardize the inputs
    """
    return inp.lower()
def bootstrap():
    """
    make a config file
    """
    os.chdir('/etc')
    if os.path.exists('gupm.json'):
        os.remove('gupm.json')
    file = open('gupm.json', 'w+')
    ops = str(input('what is your os [a]rch / [u]buntu / [f]edora : '))
    if normalize(ops) in ['f', 'u', 'a']:
        json.dump({'os':normalize(ops)}, file)
        print('saved')
    else:
        print("you're input is ****")

def install(package, config):
    """
    install package
    """
    if config["os"] == 'u':
        os.system(f"apt install {package}")
    elif config["os"] == 'f':
        os.system(f"dnf install {package}")
    elif config["os"] == 'a':
        os.system(f"pacman -S {package}")

def remove(package, config):
    """
    remove packages
    """
    if config["os"] == 'u':
        os.system(f"apt remove {package}")
    elif config["os"] == 'f':
        os.system(f"dnf remove {package}")
    elif config["os"] == 'a':
        os.system(f"pacman -R {package}")  
        
def upgradepackage(package, config):
    """
    upgrade package
    """
    if config["os"] == 'u':
        os.system(f"apt upgrade {package}") #TODO:it suggests to upgrade other packages 
    elif config["os"] == 'f':
        os.system(f"dnf install {package}") #it will update if there was a new version
    elif config["os"] == 'a':
        os.system(f"pacman -S {package}") #it will update if there was a new version
     
if __name__ == "__main__":
    if sys.argv[1] == 'setup':
        bootstrap()
    else:
        os.chdir('/etc')
        FILE = open('gupm.json', 'r')
        CONFIG = json.load(FILE)
        if sys.argv[1] == 'install':
            install(sys.argv[2], CONFIG)
        elif sys.argv[1] == 'remove':
            remove(sys.argv[2], CONFIG)
        elif sys.argv[1] == 'up':
            upgradepackage(sys.argv[2], CONFIG)
        