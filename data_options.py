from tkinter import *
import csv_converter as csv

root = Tk()
root.title("Tk dropdown example")
tkvar = StringVar(root)

def change_dropdown(*args):
    print(tkvar.get())

def build():
    
    # Add a grid
    mainframe = Frame(root)
    mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)

    # List with options
    choices = csv.getvals()
    tkvar.set(choices[0]) # set the default option

    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text="Please select a subset of student data.").grid(row = 1, column = 1)
    popupMenu.grid(row = 2, column =1)

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)

    root.mainloop()
