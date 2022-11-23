from tkinter import *
from tkinter import messagebox
import mysql.connector


def calculatefairbookinguserwin():
    def calculation():
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="soley2000",
            database="starmoversdb"
        )

        conn = con.cursor()
        q = "SELECT * FROM faredetail  WHERE transporttype = %s "
        transporttype = transportTypeE.get()
        kg = int(E1.get())
        km = int(E2.get())
        width = int(E3.get())
        height =int(E4.get())

        tpdata = (transporttype,)
        conn.execute(q,tpdata)
        data = conn.fetchone()

        if conn.rowcount == 1:
            # print(data)
            # print("CHAREGE PER KG =>", data[2])
            # print("CHARGE PER KM =>", data[3])
            # print("CHARGE PER WIDTH =>", data[4])
            # print("CHARGE PER HEIGHT =>", data[5])
            total_amt =( (data[2] * kg) + (data[3]* km) + (data[4] * width) + (data[5] * height) )
            print(total_amt)
            totalE.insert(0,str(total_amt))
        else:
            messagebox.showinfo("failed","No Such Record")





    calwin = Tk()
    calwin.geometry("400x400")
    calwin.title("calculator window")
    transportType = Label(calwin, text = " type of goods")
    transportTypeE = Entry(calwin)
    l1 = Label(calwin,text="weigth of goods in KG ")
    E1 = Entry(calwin)

    l2 = Label(calwin,text="distance in KM ")
    E2 = Entry(calwin)

    l3 = Label(calwin,text="Height of goods in feet ")
    E3 = Entry(calwin)

    l4 = Label(calwin,text="width of goods in feet ")
    E4 = Entry(calwin)

    btn = Button(calwin , text = " calculate",command = calculation)
    totalL = Label(calwin, text ="total amount")
    totalE = Entry(calwin)


    transportType.pack()
    transportTypeE.pack()
    l1.pack()
    E1.pack()
    l2.pack()
    E2.pack()
    l3.pack()
    E3.pack()
    l4.pack()
    E4.pack()
    btn.pack()
    totalL.pack()
    totalE.pack()


    calwin.mainloop()

