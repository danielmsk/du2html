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

    def convert_html_from_one_du(self, infile):
        du = DUResult(infile)
        renderer =  HTMLRenderer(du, infile, self.opt['totalsize'])
        renderer.render(self.out, self.opt['innerpath'])

        self.log.info('SAVED.. ' + self.out)

    def dispatch(self):
        if self.opt['in'] is not None:
            self.convert_html_from_one_du(self.opt['in'])

        # if self.opt['path'] is not None:
        #     self.save_data_with_userinput_udilist()
        #     self.opt['log'].info('GENERATED INDEX FILES: ')