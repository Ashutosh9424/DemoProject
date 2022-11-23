from tkinter import*
from tkinter import messagebox
import mysql.connector

def conCheck():
    con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="soley2000"
        database="ramadb"

    )
    if con:
        messagebox.showinfo("Success","Connection Done")
    else:
        messagebox.showinfo("failed","connection failed")
mw=Tk()

conBtn=Button(text="Connect",command=conCheck)
conBtn.pack()
mw.mainloop()