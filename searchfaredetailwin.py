from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector


def searchfaredetailuserwin():
    def search():
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="soley2000",
            database="starmoversdb"
        )
        if con:
            messagebox.showinfo('connection info', 'connection done')

            transporttype = tsptypeen.get()

            cur = con.cursor()
            query = "select *from faredetail where transporttype=%s"

            tpdata = (transporttype,)
            cur.execute(query, tpdata)
            data = cur.fetchone()

            mw3.wm_withdraw()
            mw4 = Tk()
            mw4.title('search details')
            mw4.geometry("400x400")
            idlb = Label(mw4, text="id")
            tptypelb = Label(mw4, text="Transport type")
            chrgkglb = Label(mw4, text="Charge per kg")
            chrgkmlb = Label(mw4, text="Charge per km")
            chrgwdlb = Label(mw4, text="Charge per width")
            chrghtlb = Label(mw4, text="Charge per height")
            iden = Entry(mw4)
            tptypeen = Entry(mw4)
            chrgkgen = Entry(mw4)
            chrgkmen = Entry(mw4)
            chrgwden = Entry(mw4)
            chrghten = Entry(mw4)
            iden.insert(0, data[0])
            tptypeen.insert(0, data[1])
            chrgkgen.insert(0, data[2])
            chrgkmen.insert(0, data[3])
            chrgwden.insert(0, data[4])
            chrghten.insert(0, data[5])
            idlb.place(x=0, y=10)
            iden.place(x=100, y=10)
            tptypelb.place(x=0, y=40)
            tptypeen.place(x=100, y=40)
            chrgkglb.place(x=0, y=70)
            chrgkgen.place(x=100, y=70)
            chrgkmlb.place(x=0, y=110)
            chrgkmen.place(x=100, y=110)
            chrgwdlb.place(x=0, y=140)
            chrgwden.place(x=100, y=140)
            chrghtlb.place(x=0, y=170)
            chrghten.place(x=100, y=170)
            mw4.mainloop()

        else:
            messagebox.showinfo('connection info', 'connection failed')

    mw3 = Tk()
    mw3.title("Fare details")
    mw3.geometry("400x400")

    tsptypelb = Label(mw3, text="Transport type")

    tsptypeen = Entry(mw3)

    tsptypelb.place(x=0, y=40)
    tsptypeen.place(x=100, y=40)

    btn = Button(mw3, text="Search Details", command=search)
    btn.place(x=80, y=210)
    mw3.mainloop()