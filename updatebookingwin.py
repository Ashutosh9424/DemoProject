from tkinter import *
from tkinter import messagebox
import mysql.connector


def updatebookinguserwin():
    def newWinForUpdate():

        def editC():


            con = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="soley2000",  # type here your password
                db="starmoversdb"
            )

            if con != None:
                print("connection done")
                cur = con.cursor()


                sql = " UPDATE `bookingdetail` SET  bookingdate =%s ,`From` = %s, `to` = %s , goodsdetail=%s , ratebyperkm = %s , ratebyperkg = %s , customername = %s,customermob = %s , customeraddress = %s , customerid = %s , status = %s,bookingchargewidth = %s , bookingchargeheight=%s WHERE (bookingid = %s and username =%s )";

                #execute()#receive data always in the form of tuple
                bookingdate = E2.get()
                username = j
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
                bookingid = i


                data = (bookingdate,From,to,goodsdetail,ratebyperkm,ratebyperkg,customername,customermob,customeraddress, customerid,status,bookingchargewidth,bookingchargeheight,bookingid ,username)
                cur.execute(sql, data)
                con.commit()
                if cur.rowcount == 1:
                    print("Updated Successfully")
                    messagebox.showinfo("info", "Updated Successfully")
                else:
                    print("failed to update ")
                    messagebox.showinfo("info", "failed to update ")

        up = Tk()
        up.geometry("700x700")
        up.title("update")

        l2 = Label(up, text="BOOKING DATE ")
        E2 = Entry(up)

        #l3 = Label(up, text="USERNAME ")
        #E3 = Entry(up)

        l4 = Label(up, text="FROM ")
        E4 = Entry(up)

        l5 = Label(up, text="TO ")
        E5 = Entry(up)

        l6 = Label(up, text="GOODS DETAILS ")
        E6 = Entry(up)

        l7 = Label(up, text="RATE BY PER KM ")
        E7 = Entry(up)

        l8 = Label(up, text="RATE BY PER KG ")
        E8 = Entry(up)

        l9 = Label(up, text="CUSTOMER NAME ")
        E9 = Entry(up)

        l10 = Label(up, text="CONTACT NO. ")
        E10 = Entry(up)

        l11 = Label(up, text="ADDRESS ")
        E11 = Entry(up)

        l12 = Label(up, text="CUSTOMER ID ")
        E12 = Entry(up)

        l13 = Label(up, text="STATUS ")
        E13 = Entry(up)

        l14 = Label(up, text="BOOKING CHARGE WIDTH ")
        E14 = Entry(up)

        l15 = Label(up, text="BOOKING CHARGE HEIGHT ")
        E15 = Entry(up)

        submitBtn = Button(up, text="Submit", command=editC)

        heading.place(x=200, y=50)



        l2.place(x=100, y=130)
        E2.place(x=250, y=130)

        l4.place(x=100, y=190)
        E4.place(x=250, y=190)

       # l3.place(x=100, y=160)
        #E3.place(x=250, y=160)

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

        up.mainloop()

    def check():
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="starmoversdb"

        )
        if con:
            messagebox.showinfo("Success", "Connection Done")
            # input
            bookingid  = BidE.get()
            username = userE.get()
            global i , j
            i = bookingid
            j = username


            # database(fetch)
            qry = "SELECT * FROM bookingdetail where bookingid=%s and username=%s"

            tpdata = (bookingid, username)

            cur = con.cursor()
            cur.execute(qry, tpdata)
            data = cur.fetchone()
            if data != None:
                edit.wm_withdraw()
                newWinForUpdate()

            else:
                messagebox.showinfo("info", "Incorrect Input")

        else:
            messagebox.showinfo("Success", "NO Done")



    edit = Tk()
    edit.geometry("300x300+20+20")
    edit.resizable(0,0)
    edit.title("EDIT DETAILS")

    heading = Label(edit,text = "Enter your Username And contact number for edit details")
    BidL = Label(edit, text="Booking Id NUMBER : ")
    userL = Label(edit, text="USERNAME : ")

    BidE= Entry(edit)
    userE = Entry(edit)



    okB = Button(edit,text = "ok", command = check)
    heading.place(x=30,y=20)
    BidL.place(x=40, y=50)
    BidE.place(x=100, y=50)
    userL.place(x= 40 ,y = 90 )
    userE.place(x=100 , y = 90)

    okB . place(x =120 , y = 170)

    edit.mainloop()

