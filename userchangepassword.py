from tkinter import *
from tkinter import messagebox
import mysql.connector


def userchangepassuserwin():
    def adam():
        conad = mysql.connector.connect(
            host="localhost",
            user="root",
            password="soley2000",
            database="starmoversdb"

        )
        if conad:
            cursor = conad.cursor()
            qry = "UPDATE starmoversdb.users SET name = %s, password = %s, usertype = %s WHERE (id = %s)"
            id = e1.get()
            name = e2.get()
            password = e3.get()
            usertype = e4.get()
            cursor.execute(qry, [name, password, usertype, id])
            conad.commit()
            results = cursor.fetchall()
            if results != None:
                messagebox.showinfo("", "Update Success")
                root.destroy()
                # adminmainwin()
                return True
            else:
                messagebox.showinfo("", "Incorrect Name and Password")
                return False
        else:
            messagebox.showinfo("failed", "connection failed")


    root = Tk()
    root.title("Admin Change Password")
    root.geometry("400x300")
    global e1
    global e2
    global e3
    global e4

    Label(root, text="id").place(x=10, y=10)
    Label(root, text="name").place(x=10, y=40)
    Label(root, text="password").place(x=10, y=70)
    Label(root, text="usertype").place(x=10, y=100)

    e1 = Entry(root)
    e1.place(x=140, y=10)

    e2 = Entry(root)
    e2.place(x=140, y=40)

    e3 = Entry(root)
    e3.place(x=140, y=70)
    e3.config(show="*")

    e4 = Entry(root)
    e4.place(x=140, y=100)

    Button(root, text="Update", command=adam, height=2, width=10).place(x=10, y=130)
    root.mainloop()

