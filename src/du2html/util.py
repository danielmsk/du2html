import os
import re
import csv
import du2html


def sortdict(d, asc="asc"):
    diclist = []
    for i in d.keys():
        diclist.append((i, d[i]))
    if asc == "asc":
        # diclist.sort(key=lambda(x,y):y)    ### for python2
        diclist.sort(key=lambda x: x[1])
    else:
        # diclist.sort(key=lambda(x,y):y, reverse=True)   ### for python2
        diclist.sort(key=lambda x: x[1], reverse=True)

    keys = []
    values = []
    for i in diclist:
        keys.append(i[0])
        values.append(i[1])
    return (keys, values)

def fileOpen(path):
    f = open(path, "r")
    return f.read()

def getTemplatePath(tempfile):
    return (os.path.join(du2html.__path__[0], 'templates', tempfile))

def renderTemplate(templatefile, outfile, data={}):
    cont = fileOpen(getTemplatePath(templatefile))
    for k1 in data.keys():
        cont = cont.replace('##' + k1+ '##', data[k1])
    fileSave(outfile, cont, 'w')

def comma(value):
    return "{:,}".format(value)

def humanreadable_filesize(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def fileSave(path, cont, opt, encoding='utf-8', gzip_flag="n"):
    if gzip_flag == "gz":
        import gzip
        if not "b" in opt:
            opt += "b"
        f = gzip.open(path, opt)
        f.write(cont.encode())
        f.close()
    else:
        f = open(path, opt, encoding=encoding)
        f.write(cont)
        f.close

################################################

def walk(dirPath, ext=""):
    flist = []
    for root, dirs, files in os.walk(dirPath):
        for fname in files:
            if (len(ext) > 0 and fname.endswith(ext)) or len(ext) == 0:
                fullpath = os.path.join(root, fname)
                flist.append(fullpath)
    flist.sort()
    return flist


class DommyLog:
    def __init__(self):
        pass

    def info(self, msg):
        print(msg)
    
    def error(self, msg):
        print(msg)