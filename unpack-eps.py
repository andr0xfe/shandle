#-*-coding:utf-8-*-
"""
filemagic.py
"""

__author__ = "andr.0xfe"
__date__ = '18:42 2017/12/20'

import sys
import os

import argparse

import zlib




# https://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check

def handle_file(file):
    with open(file, 'rb') as f:
        with open(file+"_shellcode",'wb') as shellcode:
            shellcode.write(zlib.decompress(f.read(),-zlib.MAX_WBITS))

def unpack(path):
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
    unpack(sys.argv[1])



if __name__ == "__main__":
    main()

    