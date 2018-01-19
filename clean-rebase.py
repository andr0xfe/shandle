#-*-coding:utf-8-*-
"""
clean-rebase.py
清理pe文件的基址重定位
"""

__author__ = "andr.0xfe"
__date__ = '10:22 2017/12/29'

import sys
import os

import argparse

import pefile


def clean(path):
    """
    docstring here
        :param file: file or dir
    """
    def handle_file(file):
        with pefile.PE(file) as pe:
            pe.set_word_at_offset(0,0)
            
        


    if os.path.isfile(path):
        return handle_file(path)
    else:
        [handle_file(os.path.join(t[0], file)) for t in os.walk(path) for file in t[2]  ]

def main():

    # cmd
    parser = argparse.ArgumentParser()
    parser.add_argument('path', action='store', help='需要清理基址重定位的pe文件或dir')
    if len(sys.argv) < 2:
        parser.print_help()
        exit()
    
    # handle
    clean(sys.argv[1])



if __name__ == "__main__":
    main()

    