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

def strip_tag(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)

def get_patterns_from_terms(terms):
    patterns = []
    for term in terms:
        patterns.append(convert_term2pattern(term))
    return patterns

def convert_term2pattern(term):
    aterm = ""
    if term[0] == "*":
        if term[-1] == "*":
            aterm += term[1:-1]
        else:
            aterm += term[1:] + r'\b'
    else:
        if term[-1] == "*":
            aterm += r'\b' + term[:-1]
        else:
            aterm += r'\b' + term + r'\b'
    return aterm

def save_csv(out, data):
    with open(out, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def check_ext(out, ext):
    dext = ext
    if dext[0] != '.':
        dext = '.' + ext
    if not out.endswith(ext):
        out += ext 
    return out

def getpath(filename):
    return os.path.split(os.path.abspath(filename))

def readhead(filename):
    arr = []
    for line in open(filename):
        arr = line.split('\t')
        arr[-1] = arr[-1].strip()
        break
    return arr

def gzopen(fname):
    if fname.endswith(".gz"):
        import gzip
        f1 = gzip.GzipFile(fname, "r")
    else:
        f1 = open(fname)
    return f1

def run_cmd(scmd, flag=False):
    if flag:
        print(scmd)
    rst = os.popen(scmd)
    rst_cont = rst.read()
    return rst_cont

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

def is_exist(fpath):
    return os.path.exists(fpath)


def decodeb(bstr):
    if type(bstr) == type(b'a'):
        rst = bstr.decode('UTF-8')
    else:
        rst = bstr
    return rst

def convert_rudi_to_udi(rudi):
    arr = rudi.replace('f.','').split('.')
    udi = arr[0] + '-' + '.'.join(arr[1:])
    return udi

def convert_udi_to_rudi(udi):
    return 'f.'+udi.replace('-','.')

class DommyLog:
    def __init__(self):
        pass

    def info(self, msg):
        print(msg)
    
    def error(self, msg):
        print(msg)