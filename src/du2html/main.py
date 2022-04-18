import os
import time
import re
from . import util
from .duresult import DUResult
from .render import HTMLRenderer

class DU2HTML():
    opt = None
    out = ""
    log = util.DommyLog()

    def __init__(self, opt):
        self.opt = opt
        self.has_opt_error = False
        self.out = self.opt['out']
        self.log = self.opt['log']
        if self.out == "":
            self.out = self.opt['in'] + '.html'
        self.renderer = None

    def run(self):
        self.opt['log'].info('COMMAND: ' + self.opt['cmd'])
        t0 = time.time()
        self.dispatch()
        t2 = time.time()

        self.opt['log'].info('Total running time: ' + str(round(t2-t0, 1))+' sec')
        self.opt['log'].info('END')

    def get_humanreadable_size(self, totalsize):
        rst = totalsize
        if rst is not None:
            if rst[-1].lower() == "b":
                rst = rst[:-1]
            last = rst[-1].lower()
            if last == 'k' or last == 'm' or last == 'g':
                try:
                    numsize = int(rst[:-1].replace(',',''))
                    if last == 'k':
                        numsize = numsize*1024
                    if last == 'm':
                        numsize = numsize*1024*1024
                    if last == 'g':
                        numsize = numsize*1024*1024*1024
                    rst = util.humanreadable_filesize(numsize)
                except ValueError:
                    rst = totalsize
            else:
                try:
                    rst = util.humanreadable_filesize(int(totalsize.replace(',','')))
                except ValueError:
                    rst = totalsize
        return rst

    def convert_html_from_one_du(self, infile):
        du = DUResult(infile)
        renderer =  HTMLRenderer(du, infile, self.get_humanreadable_size(self.opt['totalsize']) )
        renderer.render(self.out, self.opt['innerpath'])

        self.log.info('SAVED.. ' + self.out)

    def dispatch(self):
        if self.opt['in'] is not None:
            self.convert_html_from_one_du(self.opt['in'])

        # if self.opt['path'] is not None:
        #     self.save_data_with_userinput_udilist()
        #     self.opt['log'].info('GENERATED INDEX FILES: ')