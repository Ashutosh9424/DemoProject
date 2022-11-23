from tkinter import *
from tkinter import messagebox
import mysql.connector
from adminmainwin import adminstartwin
# from checkimage import label1
from usermainwin import userstartwin
from PIL import ImageTk, Image
from PIL import Image, ImageTk


def adminLogin():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="soley2000",
        database="starmoversdb"

    )
    if con:
        messagebox.showinfo("Success", "Connection Done")
        # input
        inname = enname.get()
        inpass = enpass.get()
        # database(fetch)
        qry = "SELECT *FROM users where name=%s and password=%s and usertype='admin'"
        tpdata = (inname, inpass)
        cur = con.cursor()
        cur.execute(qry, tpdata)  ### cur.table id name password
        # 101 Sumit verma 6666
        data = cur.fetchone()
        if data != None:
            mw.wm_withdraw()
            adminstartwin()

        else:
            messagebox.showinfo("info", "login failed")

    else:
        messagebox.showinfo("failed", "connection failed")


def userLogin():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="soley2000",
        database="starmoversdb"

    )
    if con:
        messagebox.showinfo("Success", "Connection Done")
        # input
        inname = enname.get()
        inpass = enpass.get()
        # database(fetch)
        qry = "SELECT *FROM users where name=%s and password=%s and usertype='user'"
        tpdata = (inname, inpass)
        cur = con.cursor()
        cur.execute(qry, tpdata)  ### cur.table id name password
        # 101 Sumit verma 6666
        data = cur.fetchone()
        if data != None:
            mw.wm_withdraw()
            userstartwin()

        else:
            messagebox.showinfo("info", "login failed")

    else:
        messagebox.showinfo("failed", "connection failed")


mw = Tk()
mw.geometry("800x400")
lbname = Label(mw, text="Enter Name     ")
lbpass = Label(mw, text="Enter Password    ")
enname = Entry(mw)
enpass = Entry(mw, show="*")

adminLoginBtn = Button(text="AdminLogin", command=adminLogin)
userLoginBtn = Button(text="UserLogin", command=userLogin)

# lbname.grid(row=0,column=0)
#
# enname.grid(row=0,column=1)
# lbpass.grid(row=1,column=0)
#
# enpass.grid(row=1,column=1)
# adminLoginBtn.grid(row=4, column=0)
# userLoginBtn.grid(row=4, column=1)

# lbname.place(x=80, y=130)
# enname.place(x=200,y=130)

image = Image.open("second.jpg")

# Resize the image using resize() method
resize_image = image.resize((150, 150))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
Label(image=img).place(x=50, y=50)


mw.mainloop()
