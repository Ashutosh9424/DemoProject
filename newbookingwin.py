from tkinter import *
from tkinter import messagebox
import mysql.connector


def newbookinguserwin():
    def create_fun():
        # insert query
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="soley2000",
            db="starmoversdb"
        )
        if con != None:
            print("connection done")
            cur = con.cursor()
            sql = " INSERT INTO `bookingdetail` (`bookingdate`, `username`, `from`, `to`, `goodsdetail`, `ratebyperkm`, `ratebyperkg`, `customername`, `customermobno`, `customeraddress`, `customerid`, `status`, `bookingchargewidth`, `bookingchargeheight`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)";

            # bookingid= E1.get()
            bookingdate = E2.get()
            username = E3.get()
            From = E4.get()
            to = E5.get()
            goodsdetail = E6.get()
            ratebyperkm = E7.get()
            ratebyperkg = E8.get()
            customername = E9.get()
            customermob = E10.get()
            customeraddress = E11.get()
            customerid = E12.get()
            status = E13.get()
            bookingchargewidth = E14.get()
            bookingchargeheight = E15.get()

            if (
                    bookingdate and username and From and to and goodsdetail and ratebyperkm and ratebyperkg and customername and customermob and customeraddress and customerid and status and bookingchargewidth and bookingchargeheight) != " ":
                tpdata = (
                bookingdate, username, From, to, goodsdetail, ratebyperkm, ratebyperkg, customername, customermob,
                customeraddress, customerid, status, bookingchargewidth, bookingchargeheight)
                cur.execute(sql, tpdata)
                con.commit()
                if cur.rowcount == 1:
                    messagebox.showinfo("info", "BOOKED")

                else:
                    messagebox.showinfo("info", "Please Try Later")
                con.close()
            else:
                messagebox.showinfo("info", "please fill the information")

        # *****************************************************************************************************************************#

    bw = Tk()
    bw.geometry("500x680")
    bw.title("Booking Window")
    heading = Label(bw, text="BOOKING  DETAILS")  # center

    # l1 = Label(bw,text = "BOOKING ID ")   # autoincremented
    # E1 = Entry(bw)

    l2 = Label(bw, text="BOOKING DATE ")
    E2 = Entry(bw)

    l3 = Label(bw, text="USERNAME ")
    E3 = Entry(bw)

    l4 = Label(bw, text="FROM ")
    E4 = Entry(bw)

    l5 = Label(bw, text="TO ")
    E5 = Entry(bw)

    l6 = Label(bw, text="GOODS DETAILS ")
    E6 = Entry(bw)

    l7 = Label(bw, text="RATE BY PER KM ")
    E7 = Entry(bw)

    l8 = Label(bw, text="RATE BY PER KG ")
    E8 = Entry(bw)

    l9 = Label(bw, text="CUSTOMER NAME ")
    E9 = Entry(bw)

    l10 = Label(bw, text="CONTACT NO. ")
    E10 = Entry(bw)

    l11 = Label(bw, text="ADDRESS ")
    E11 = Entry(bw)

    l12 = Label(bw, text="CUSTOMER ID ")
    E12 = Entry(bw)

    l13 = Label(bw, text="STATUS ")
    E13 = Entry(bw)

    l14 = Label(bw, text="BOOKING CHARGE WIDTH ")
    E14 = Entry(bw)

    l15 = Label(bw, text="BOOKING CHARGE HEIGHT ")
    E15 = Entry(bw)

    submitBtn = Button(bw, text="Submit", command=create_fun)

    heading.place(x=200, y=50)

    # l1.place(x=100 , y = 100)
    # E1.place(x=250, y =100)

    l2.place(x=100, y=130)
    E2.place(x=250, y=130)

    l3.place(x=100, y=160)
    E3.place(x=250, y=160)

    l4.place(x=100, y=190)
    E4.place(x=250, y=190)

    l5.place(x=100, y=220)
    E5.place(x=250, y=220)

    l6.place(x=100, y=250)
    E6.place(x=250, y=250)

    l7.place(x=100, y=280)
    E7.place(x=250, y=280)

    l8.place(x=100, y=320)
    E8.place(x=250, y=320)

    l9.place(x=100, y=350)
    E9.place(x=250, y=350)

    l10.place(x=100, y=380)
    E10.place(x=250, y=380)

    l11.place(x=100, y=420)
    E11.place(x=250, y=420)

    l12.place(x=100, y=450)
    E12.place(x=250, y=450)

    l13.place(x=100, y=480)
    E13.place(x=250, y=480)

    l14.place(x=100, y=520)
    E14.place(x=250, y=520)

    l15.place(x=100, y=550)
    E15.place(x=250, y=550)

    submitBtn.place(x=250, y=600)

    bw.mainloop()

