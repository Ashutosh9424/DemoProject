from tkinter import *
from tkinter import messagebox
import mysql.connector


def searchfairbookinguserwin():
    def find():
        find = Tk()
        find.geometry("400x400")

        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="soley2000",
            db="starmoversdb"
        )

        if con != None:
            cur = con.cursor()
            q = " SELECT * FROM faredetail where transporttype = %s "
            transporttype = E1.get()
            tpdata = (transporttype,)

            cur.execute(q, tpdata)
            print("type ", type(cur))
            data = cur.fetchone()
            l1 = Label(find, text="id")
            l2 = Label(find, text="transporttype")
            l3 = Label(find, text="chargeperkg")
            l4 = Label(find, text="chargeperkm")
            l5 = Label(find, text="chargewidth")
            l6 = Label(find, text="chargeheight")
            t = (l1, l2, l3, l4, l5, l6)

            p = 0
            for k in t:
                k.grid(row=0, column=p)
                p = p + 1

            if cur.rowcount == 1:
                j = 0
                for i in data:
                    e = Entry(find, width=10)
                    e.grid(row=1, column=j)
                    e.insert(END, i)
                    j = j + 1
            else:
                messagebox.showinfo("info", "No Record Found")

        find.mainloop()

    search = Tk()
    search.geometry("400x400")
    search.title("search fare")

    L1 = Label(search, text="Enter Transport Type")
    E1 = Entry(search)

    Btn = Button(search, text=" Search", command=find)

    L1.place(x=20, y=50)
    E1.place(x=100, y=50)
    Btn.place(x=100, y=100)

    search.mainloop()

