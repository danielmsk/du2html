from . import util

REPORT_MAX_LEVEL = 2

class Directory:
    path = ""
    id = 0
    size = 0
    level = 9999
    arrpath = []
    arrpath_wo_root = []
    childlist = []
    rootpath = ""

    def __init__(self, path, size, id):
        self.path = path
        self.arrpath = self.path.split('/')
        self.title = self.arrpath[-1]
        self.size = size * 1000
        self.id = id
        self.rootpath = ""
        self.childlist = []
        self.arrpath_wo_root = []
        self.parentpath = '/'.join(self.arrpath[:-1])

    def __str__ (self):
        return '\t'.join([str(self.level), str(self.size), self.path])

    def set_rootpath(self, rootpath):
        self.rootpath = rootpath
        if self.path == self.rootpath:
            self.level = 0
        else:
            tmppath = self.path[len(self.rootpath):]
            if tmppath[0] == "/":
                tmppath = tmppath[1:]
            self.arrpath_wo_root = tmppath.split('/')
            self.level = len(self.arrpath_wo_root)

    def sort_childlist(self, asc="desc"):
        sizemap = {}
        childmap = {}
        for d1 in self.childlist:
            sizemap[d1.path] = d1.size
            childmap[d1.path] = d1

        sorted_childlist = []
        (ks, vs) = util.sortdict(sizemap, asc)
        for k1 in ks:
            sorted_childlist.append(childmap[k1])
        self.childlist = sorted_childlist



class DUResult:
    infile = None 
    dirlist = []
    root = None
    rootpath = ""
    report_max_level = REPORT_MAX_LEVEL

    def __init__(self, infile, report_max_level=REPORT_MAX_LEVEL):
        self.infile = infile
        self.dirlist = []
        self.report_max_level = report_max_level
        self.rootpath = ""
        self.root = None
        self.load()

    def set_rootpath(self):
        line = ""
        for l1 in open(self.infile, "r", encoding="UTF-8", errors='ignore'):
            line = l1
        arr = line.split('\t')
        self.rootpath = arr[-1].strip()

    def get_level(self, path):
        tmppath = path[len(self.rootpath):]
        if self.rootpath == path:
            level = 0
        elif tmppath[0] == "/":
            level = len(tmppath[1:].split('/'))
        return level


    def load(self):
        self.set_rootpath()
        id = 0
        for line in open(self.infile, "r", encoding="UTF-8", errors='ignore'):
            arr = line.split('\t')
            size = int(arr[0])
            path = arr[-1].strip()
            level = self.get_level(path)

            if level <= self.report_max_level:
                id += 1
                d1 = Directory(path, size, id)
                d1.set_rootpath(self.rootpath)
                self.dirlist.append(d1)

        self.restructurize_list()
        # self.printlist()

    def restructurize_list(self):
        dirmap = {}
        for i in range(len(self.dirlist)-1, -1, -1):
            d1 = self.dirlist[i]
            if d1.level <= self.report_max_level: 
                dirmap[d1.path] = d1
                if d1.level == 0:
                    self.root = d1
                else:
                    dirmap[d1.parentpath].childlist.append(d1)
        

    def printlist(self):
        for d1 in self.dirlist:
            print(d1)