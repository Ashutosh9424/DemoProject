from tkinter import *
from tkinter import messagebox
import mysql.connector


def showfairbookinguserwin():
    show = Tk()
    show.geometry("400x250")
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="soley2000",
        database="starmoversdb"

    )
    my_conn = con.cursor()
    q = "SELECT * FROM faredetail "
    my_conn.execute(q)

    l1 = Label(show, text="id")
    l2 = Label(show, text="transporttype")
    l3 = Label(show, text="chargeperkg")
    l4 = Label(show, text="chargeperkm")
    l5 = Label(show, text="chargewidth")
    l6 = Label(show, text="chargeheight")
    t = (l1, l2, l3, l4, l5, l6)

    p = 0
    for k in t:
        k.grid(row=0, column=p)
        p = p + 1
    i = 1

    for each_record in my_conn:
        for j in range(len(each_record)):
            e = Entry(show, width=10)  # width=10, fg='blue'
            e.grid(row=i, column=j)
            e.insert(END, each_record[j])
        i = i + 1

    show.mainloop()
