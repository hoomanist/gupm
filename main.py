import argparse
import os
import commands
parser = argparse.ArgumentParser()

parser.add_argument("install",help="install packages")

args = parser.parse_args()
if os.name == "posix":
    if args.install:
        commands.install()
    else :
        print("not supported")
else:
    print("this is for unix like systems")