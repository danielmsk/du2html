from . import util

REPORT_MAX_LEVEL = 3

class Directory:
    path = ""
    id = 0
    size = 0
    level = 9999
    arrpath = []
    childlist = []

    def __init__(self, path, size, level, id):
        self.path = path
        self.arrpath = self.path.split('/')
        self.title = self.arrpath[-1]
        self.size = size * 1000
        self.level = level
        self.id = id
        self.childlist = []
        self.parentpath = '/'.join(self.arrpath[:-1])

    def __str__ (self):
        return '\t'.join([str(self.level), str(self.size), self.path])


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
    report_max_level = REPORT_MAX_LEVEL

    def __init__(self, infile, report_max_level=REPORT_MAX_LEVEL):
        self.infile = infile
        self.dirlist = []
        self.report_max_level = report_max_level
        self.root = None
        self.load()

    def load(self):
        id = 0
        for line in open(self.infile, "r", encoding="UTF-8", errors='ignore'):
            arr = line.split('\t')
            arr[-1] = arr[-1].strip()
            size = int(arr[0])
            path = arr[1]
            arrpath = path.split('/')
            level = len(arrpath)

            if level <= self.report_max_level:
                id += 1
                self.dirlist.append(Directory(path, size, level, id))

        self.restructurize_list()
        # self.printlist()

    def restructurize_list(self):
        dirmap = {}
        for i in range(len(self.dirlist)-1, -1, -1):
            d1 = self.dirlist[i]
            dirmap[d1.path] = d1
            if d1.level == 1:
                self.root = d1
            else:
                dirmap[d1.parentpath].childlist.append(d1)
        
        # self.root.sort_childlist()
        # for d1 in self.root.childlist:
        #     print(d1)

    def printlist(self):
        for d1 in self.dirlist:
            print(d1)