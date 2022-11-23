from tkinter import *
from tkinter import messagebox
import mysql.connector


def openbookinguserwin():
    my_w = Tk()
    my_w.geometry("400x250")
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="soley2000",
        database="starmoversdb"

    )
    my_conn = con.cursor()
    q = "SELECT * FROM bookingdetail "
    ####### end of connection ####
    my_conn.execute(q)

    l1 = Label(my_w, text="Booking id")
    l2 = Label(my_w, text="booking date ")
    l3 = Label(my_w, text="username ")
    l4 = Label(my_w, text="from ")
    l5 = Label(my_w, text="to")
    l6 = Label(my_w, text="goodsdetail ")
    l7 = Label(my_w, text="ratebyperkm  ")
    l8 = Label(my_w, text="ratebyperkg  ")
    l9 = Label(my_w, text="customername  ")
    l10 = Label(my_w, text="customermob  ")
    l11 = Label(my_w, text="customeraddress  ")
    l12 = Label(my_w, text="customerid  ")
    l13 = Label(my_w, text="status  ")
    l14 = Label(my_w, text="bookingchargewidth  ")
    l15 = Label(my_w, text="bookingchargeheight ")
    t = (l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15)

    p = 0
    for k in t:
        k.grid(row=0, column=p)
        p = p + 1

    i = 1
    for each_record in my_conn:
        for j in range(len(each_record)):
            e = Entry(my_w, width=10)  # width=10, fg='blue'
            e.grid(row=i, column=j)
            e.insert(END, each_record[j])
        i = i + 1
    my_w.mainloop()

