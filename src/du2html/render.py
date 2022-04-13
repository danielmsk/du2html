from . import util
import json
from . import _options



class HTMLRenderer:
    def __init__(self, duresult, infile, totalsize=None):
        self.duresult = duresult
        self.infile = infile
        self.totalsize = totalsize

    def get_size_string(self):
        size_string = util.humanreadable_filesize(self.duresult.root.size)
        if self.totalsize is not None:
            size_string += ' / ' + self.totalsize
        return size_string

    def get_size_data_child(self, this_dir, renderdata, pid):
        this_dir.sort_childlist()
        for d1 in this_dir.childlist:
            d = {}
            d['id'] = d1.id
            d['name'] = d1.path
            # d['path'] = d1.path
            # d['size'] = d1.size
            # d['per'] = str(round(d1.size*100/self.totalsize,1)) + '%'
            d['hsize'] = util.humanreadable_filesize(d1.size)
            if pid > 0:
                d['pid'] = pid

            renderdata.append(d)
            if len(d1.childlist) > 0:
                renderdata = self.get_size_data_child(d1, renderdata, d1.id)
        return renderdata

    def get_size_data(self):
        renderdata = self.get_size_data_child(self.duresult.root, [], 0)
        return renderdata


    def render(self, out, is_innerpath = False):
        data = {}
        data['TOTALSIZE'] = self.get_size_string()
        data['SIZEDATA'] = json.dumps(self.get_size_data())
        data['INFILE'] = self.infile
        data['ROOTPATH'] = self.duresult.rootpath
        data['VERSION'] = _options.OPT['VERSION']
        
        if is_innerpath:
            templatefile = 'temp_treetable_innerpath.html'
        else:
            templatefile = 'temp_treetable.html'
        util.renderTemplate(templatefile, out, data)
        