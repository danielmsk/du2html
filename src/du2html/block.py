from prettytable import PrettyTable
from .conf import COLNAMES
from . import util
class BLOCK:
    rows = []
    size = 0
    htmlfile = ""
    rdata_df = ""
    fid = ""
    description = ""

    def __init__(self, htmlfile):
        self.htmlfile = htmlfile
        self.rdatafile = ""
        self.rdata_df = {}
        self.fid = htmlfile.split('/')[-1].replace('.html', '').strip()
        self.rows = []
        self.size = 0
        self.desciption = ""

    def add(self, row):
        if len(self.rows) == 0:
            self.description = row['Description']
        self.rows.append(row)
        self.size = len(self.rows)

    def print(self):
        x = PrettyTable()
        x.field_names = COLNAMES
        for row in self.rows:
            listrow = []
            for cn in COLNAMES:
                try:
                    listrow.append(row[cn])
                except KeyError:
                    listrow.append('')
            x.add_row(listrow)
        # print(self.rows)
        print(x)

    def get_listrows(self):
        listrows = []
        for row in self.rows:
            listrow = []
            for cn in COLNAMES:
                try:
                    listrow.append(row[cn])
                except KeyError:
                    listrow.append('')
            listrows.append(listrow)
        return listrows

    def get_listudi(self):
        listudi = []
        for row in self.rows:
            listudi.append(row['UDI'])
        return listudi

    
