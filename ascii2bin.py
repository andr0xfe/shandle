#-*-coding:utf-8-*-
"""
ascii2bin.py
"""

__author__ = "andr.0xfe"
__date__ = '2018/12/19'

import sys
import os

import argparse

import binascii




def handle_file(file):
    with open(file, 'r') as f:
        with open(file+"_bin",'wb') as shellcode:
            shellcode.write(binascii.a2b_hex(f.read()))

def handle(path):
    """
    docstring here
        :param file: file or dir
    """
    if os.path.isfile(path):
        return handle_file(path)
    else:
        [ handle_file( os.path.join(t[0], file)) for t in os.walk(path) for file in t[2]  ]


def main():

    # cmd
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', action='store', help='需要解压的目录')
    if len(sys.argv) < 2:
        parser.print_help()
        exit()
    
    # handle
    handle(sys.argv[1])



if __name__ == "__main__":
    main()

    
