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

from tkinter import *
from tkinter import ttk

root = Tk()
l = Listbox(root, height=5)
l.grid(column=0, row=0, sticky=(N,W,E,S))
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N,S))
l['yscrollcommand'] = s.set
ttk.Label(root, text="Status message here", anchor=(W)).grid(column=0, columnspan=2, row=1, sticky=(W,E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
for i in range(1,101):
    l.insert('end', 'Line %d of 100' % i)
root.mainloop()


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
