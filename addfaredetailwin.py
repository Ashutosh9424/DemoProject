from tkinter import *
from tkinter import messagebox
import mysql.connector


def addfaredetailuserwin():
    def adam():
        conad = mysql.connector.connect(
            host="localhost",
            user="root",
            password="soley2000",
            database="starmoversdb"

        )
        if conad:
            cursor = conad.cursor()
            qry = "INSERT INTO starmoversdb.faredetail (id, transporttype, chargeperkg, chargeperkm, chargewidth, chargeheight) VALUES (%s, %s, %s, %s, %s, %s);"

            id = e1.get()
            transporttype= e2.get()
            chargeperkg = e3.get()
            chargeperkm = e4.get()
            chargewidth = e5.get()
            chargeheight = e6.get()
            cursor.execute(qry, [id, transporttype, chargeperkg, chargeperkm, chargewidth, chargeheight])
            conad.commit()
            results = cursor.fetchall()
            if results != None:
                messagebox.showinfo("", "Insert Success")
                root.destroy()
                # adminmainwin()
                return True
            else:
                messagebox.showinfo("", "Incorrect Data")
                return False
        else:
            messagebox.showinfo("failed", "connection failed")


    root = Tk()
    root.title("Add Fair Detail")
    root.geometry("600x500")
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6

    Label(root, text="id").place(x=10, y=10)
    Label(root, text="transporttype").place(x=10, y=40)
    Label(root, text="chargeperkg").place(x=10, y=70)
    Label(root, text="chargeperkm").place(x=10, y=100)
    Label(root, text="chargewidth").place(x=10, y=130)
    Label(root, text="chargeheight").place(x=10, y=160)

    e1 = Entry(root)
    e1.place(x=140, y=10)

    e2 = Entry(root)
    e2.place(x=140, y=40)

    e3 = Entry(root)
    e3.place(x=140, y=70)

    e4 = Entry(root)
    e4.place(x=140, y=100)

    e5 = Entry(root)
    e5.place(x=140, y=130)

    e6 = Entry(root)
    e6.place(x=140, y=160)

    Button(root, text="Insert", command=adam, height=2, width=10).place(x=10, y=190)
    root.mainloop()

