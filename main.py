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


if sys.argv[1] == 'setup':
    bootstrap()
