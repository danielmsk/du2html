
import re
from .conf import COLNAMES
from .block import BLOCK
from . import util



class DATA:
    html_list = []
    total_col = 0
    blocklist = []

    def __init__(self):
        self.html_list = []
        self.total_col = 0
        self.blocklist = []
        
    def set_html_list(self, path = './'):
        self.html_list = util.walk(path, '.html')

    def load_html_list(self, path = './'):
        self.set_html_list(path)

        for htmlfile in self.html_list:
            self.load_html(htmlfile)

        print("\tTotal_columns:", self.total_col)
    
    def find_htmlfile_from_fid(self, fid):
        rst = ""
        for htmlfile in self.html_list:
            if fid + '.html' in htmlfile:
                rst = htmlfile
                break
        return rst

    def load_html(self, htmlfile):
        flag = False
        no_row = 0
        no_col = 0
        block = BLOCK(htmlfile)
        for line in open(htmlfile):
            if "</table" in line:
                flag = False

            if flag:
                no_row += 1
                arr = line.strip().split('</td>')
                row = {}
                for k in range(len(arr)-1):
                    if COLNAMES[k] == "Description":
                        row[COLNAMES[k]]= util.strip_tag(arr[k].replace('<br>', ' '))
                        # print(">",arr[k])
                        # print("==>",row[COLNAMES[k]])
                    else:
                        row[COLNAMES[k]]= util.strip_tag(arr[k])
                if len(row) > 3:
                    if block.size > 0:
                        self.blocklist.append(block)
                        no_col += block.size
                    block = BLOCK(htmlfile)
                    block.add(row)
                else:
                    block.add(row)

            if not flag:
                flag2 = True
                for col in COLNAMES:
                    if not col in line:
                        flag2 = False
                if flag2:
                    flag = True
        if block.size > 0:
            self.blocklist.append(block)
            no_col += block.size

        self.total_col += no_col
        print("\tloaded", htmlfile, "no_columns:", no_col)

    def search_description(self, terms=[], logical_operator="or"):
        rst_blocklist = []

        patterns = util.get_patterns_from_terms(terms)
        
        for block in self.blocklist:
            flag_or = False
            flag_and = True
            for k in range(len(patterns)):
                fa = re.findall(patterns[k], block.description, flags=re.IGNORECASE)
                if len(fa) > 0:
                    flag_or = True
                elif len(fa) == 0:
                    flag_and = False 
            if  (logical_operator == "or" and flag_or) or (logical_operator == "and" and flag_and):
                rst_blocklist.append(block)

        return rst_blocklist
