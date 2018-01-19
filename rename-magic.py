#-*-coding:utf-8-*-
"""
filemagic.py
"""

__author__ = "andr.0xfe"
__date__ = '18:42 2017/12/20'

import sys
import os

import argparse

import magic


def rename(path):
    """
    docstring here
        :param file: file or dir
    """
    handle_file = lambda file: os.rename(file, file + '.' + \
        magic.from_file(file, mime=True).replace('/','_'))
    if os.path.isfile(path):
        return handle_file(path)
    else:
        [ handle_file( os.path.join(t[0], file)) for t in os.walk(path) for file in t[2]  ]


def main():

    # cmd
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', action='store', help='需要解析的目录')
    if len(sys.argv) < 2:
        parser.print_help()
        exit()
    
    # handle
    rename(sys.argv[1])



if __name__ == "__main__":
    main()

    