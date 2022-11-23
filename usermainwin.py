from tkinter import*
from tkinter import messagebox
import mysql.connector
from newbookingwin import newbookinguserwin
from openbookingwin import openbookinguserwin
from updatebookingwin import updatebookinguserwin
from cancelbookingwin import cancelbookinguserwin
from searchfairwin import searchfairbookinguserwin
from showfairwin import showfairbookinguserwin
from calculatefairwin import calculatefairbookinguserwin

def userstartwin():


    smw1=Tk()
    smw1.geometry("600x400+200+100")
    smw1.title("User Window")

    menubar = Menu(smw1)
    # file menu code
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=newbookinguserwin)
    filemenu.add_command(label="open", command=openbookinguserwin)
    filemenu.add_command(label="update", command=updatebookinguserwin)
    filemenu.add_command(label="cancel", command=cancelbookinguserwin)

    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=smw1.quit)

    menubar.add_cascade(label="Bookings", menu=filemenu)
    # edit menu code

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_separator()

    editmenu.add_command(label="Search", command=searchfairbookinguserwin)
    editmenu.add_command(label="show fair", command=showfairbookinguserwin)
    editmenu.add_command(label="calculate", command=calculatefairbookinguserwin)

    menubar.add_cascade(label="Calculate Fair", menu=editmenu)

    # run menu code
    smw1.config(menu=menubar)

    smw1.mainloop()