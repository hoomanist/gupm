#!/usr/bin/env python3
"""
this is not module stupid pylint
"""
import os
import sys
import json
import subprocess
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
        command = subprocess.run(['apt','install',package],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'package {package} installed')
        else:
            print(command.stderr)
    elif config["os"] == 'f':
        command = subprocess.run(['dnf','install',package, '--noconfirm'],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'package {package} installed')
        else:
            print(command.stderr) 
    elif config['os'] == 'a':
        command = subprocess.run(['pacman','-S',package],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'package {package} installed')
        else:
            print(command.stderr)
def remove(package, config):
    """
    remove packages
    """
    if config["os"] == 'u':
        command = subprocess.run(['apt','remove',package],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'package {package} removed')
        else:
            print(command.stderr)
    elif config["os"] == 'f':
        command = subprocess.run(['dnf','remove',package],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'package {package} removed')
        else:
            print(command.stderr)
    elif config["os"] == 'a':
        command = subprocess.run(['pacman','-R',package],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'package {package} removed')
        else:
            print(command.stderr)
        

def updateRepo(config):
    """
    update repository database
    """
    if config['os'] == 'u':
        command = subprocess.run(['apt', 'update'],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'repositories are updated')
        else:
            print(command.stderr)
    elif config['os'] == 'f':
        command = subprocess.run(['dnf','update'],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'repositories are updated')
        else:
            print(command.stderr)
    elif config['os'] == 'a':
        command = subprocess.run(['pacman','-Sy'],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'system is upgraded')
        else:
            print(command.stderr)


def UpgradeAllPackages(config):
    if config['os'] == 'u':
        command = subprocess.run(['apt','upgrade'],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'system is upgraded')
        else:
            print(command.stderr)

    elif config['os'] == 'f':
        command = subprocess.run(['dnf','upgrade'],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'repositories are updated')
        else:
            print(command.stderr)
    elif config['os'] ==  'a':
        command = subprocess.run(['pacman','-Syu'],stderr=subprocess.PIPE)
        if command.stderr == '':
            print(f'system is upgraded')
        else:
            print(command.stderr)

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
            install(sys.argv[2], CONFIG) # the same work
        elif sys.argv[1] == 'update':
            updateRepo(CONFIG)
        elif sys.argv[1] == 'upgrade':
            UpgradeAllPackages(CONFIG)
        
