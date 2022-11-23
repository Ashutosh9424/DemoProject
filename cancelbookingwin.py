from tkinter import *
from tkinter import messagebox
import mysql.connector


def cancelbookinguserwin():
    def cancel():
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="soley2000",  # type here your password
            db="starmoversdb"
        )
        if con != None:
            print("connection done")
            sql = "DELETE FROM bookingdetail WHERE customerid = %s";
            cur = con.cursor(prepared=True)
            customerid = E1.get()
            tpdata = (customerid ,)
            cur.execute(sql, tpdata)
            con.commit()
            if cur.rowcount == 1:
                print("Deleted Successfully")
                messagebox.showinfo("info", "Canceled Booking")
            else:
                print("No detail present ")
                messagebox.showinfo("info", "Booking Not Present ")

    dele = Tk()
    dele.title("delete window")
    dele.geometry("200x200")
    l1 = Label(dele,text ="customer id")
    E1 = Entry(dele)
    okBtn = Button(dele,text = "delete",command = cancel)

    l1.place(x=0 , y = 50)
    E1.place(x=80 , y=50)
    okBtn.place(x=100,y=100)


    dele.mainloop()


