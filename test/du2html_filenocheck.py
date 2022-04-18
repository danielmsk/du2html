#!/usr/bin/env python
# -*- coding: utf-8 -*-
#### du2html_filenocheck.py
#### made by Daniel Minseok Kwon
#### 2022-04-18 10:12:17
#########################
import sys
import os


def listdir(dirPath, ext=""):
    flist = []
    for fname in os.listdir(dirPath):
        if (len(ext) > 0 and fname.endswith(ext)) or len(ext) == 0:
            flist.append(fname)
    flist.sort()
    return flist

def run_cmd(scmd, flag=False):
    if flag:
        print(scmd)
    rst = os.popen(scmd)
    rst_cont = rst.read()
    return rst_cont

def du2html_filenocheck(path):
    dirlist = listdir(path)
    dirlist.sort()
    cnt = 0
    for fname in dirlist:
        if fname.endswith('.html'):
            cnt += 1
    
    if cnt > MAXNO:
        i = 0
        for fname in dirlist:
            if fname.endswith('.html'):
                if i < cnt - MAXNO:
                    cmd = "rm -rf " + os.path.join(path, fname)
                    run_cmd(cmd)
                    cmd = "rm -rf " + os.path.join(path, fname).replace('.html','')
                    run_cmd(cmd)
                i += 1


if __name__ == "__main__":
    MAXNO = 20   
    path = '/data/tmp/du/'
    # path = '/Users/pcaso/work/test/'
    du2html_filenocheck(path)
