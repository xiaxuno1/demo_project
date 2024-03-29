"""
tkintertable 使用
"""
import sys, os,tkintertable
from optparse import OptionParser

from tkintertable import TableCanvas
from tkintertable.App import TablesApp


def main():
    "Run the application"
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="tablefile",
                        help="Open a table file", metavar="FILE")
    opts, remainder = parser.parse_args()
    if opts.tablefile != None:
        app=TablesApp(datafile=opts.tablefile)
    else:
        app=TablesApp()
    app.mainloop()
    return


class MyTable(TableCanvas):
    """Sub-class of Tablecanvas, with some changes in behaviour to make
       a customised table - just an example"""

    def __init__(self, parent=None, model=None):
        TableCanvas.__init__(self, parent, model)
        self.cellbackgr = '#FFFAF0'
        self.entrybackgr = 'white'

        self.selectedcolor = 'yellow'
        self.rowselectedcolor = '#B0E0E6'
        self.multipleselectioncolor = '#ECD672'

        return

if __name__ == '__main__':
    MyTable()
