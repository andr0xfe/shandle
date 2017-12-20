#-*-coding:utf-8-*-
"""
filemagic.py
"""

__author__ = "hklliang"
__date__ = '$DATE $TIME'

import sys
import os

import argparse
import magic


def rename(file):
    return os.rename(file, file + '__' + magic.from_file(file, mime=True).replace('/','_'))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', action='store', help='需要解析的目录')
    if len(sys.argv) < 2:
        parser.print_help()
    #获取所有文件
    all_files = [ os.path.join(t[0], file) for t in os.walk(sys.argv[1]) for file in t[2]  ]

    #重命名
    #处理每个文件并修改文件名为  原始文件名__mime名，  '/' 替换为 _
    [ rename(file) for file in all_files]



if __name__ == "__main__":
    main()

    