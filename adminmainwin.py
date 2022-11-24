from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image

from adminchangepass import adminechangeuserwin
from createnewuser import createuserwin
from userchangepassword import userchangepassuserwin
from delete import deleteuserwin
from addfaredetailwin import addfaredetailuserwin
from searchfaredetailwin import searchfaredetailuserwin
from updatefaredetailwin import updatefaredetailuserwin
from deletefaredetailwin import deletefaredetailuserwin
from aboutprojectwin import aboutprojectuserwin
from aboutuswin import aboutususerwin


def adminstartwin():
    smw = Tk()
    smw.geometry("600x400+200+100")
    smw.title("Main Window")

    menubar = Menu(smw)
    # file menu code
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Admin Change password", command=adminechangeuserwin)
    filemenu.add_command(label="Create New User", command=createuserwin)
    filemenu.add_command(label="user Change Password", command=userchangepassuserwin)
    filemenu.add_command(label="Delete", command=deleteuserwin)

    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=smw.quit)

    menubar.add_cascade(label="Admin", menu=filemenu)
    # edit menu code

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Add FareDetail", command=addfaredetailuserwin)
    editmenu.add_command(label="Search FareDetail", command=searchfaredetailuserwin)
    editmenu.add_separator()

    editmenu.add_command(label="Update FareDetail", command=updatefaredetailuserwin)
    editmenu.add_command(label="Delete FareDetail", command=deletefaredetailuserwin)

    menubar.add_cascade(label="Fare Menu", menu=editmenu)

    # run menu code
    runmenu = Menu(menubar, tearoff=0)
    runmenu.add_command(label="About project", command=aboutprojectuserwin)
    runmenu.add_command(label="About us", command=aboutususerwin)

    menubar.add_cascade(label="Help", menu=runmenu)

    smw.config(menu=menubar)

    image = Image.open("pack.jpg")

    test = ImageTk.PhotoImage(image)

    label1 = Label(image=test)
    label1.image = test

    label1.pack()

    smw.mainloop()
