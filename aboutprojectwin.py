from tkinter import *
from tkinter import messagebox
import mysql.connector


def aboutprojectuserwin():
    smw1 = Tk()
    smw1.geometry("1000x500")
    smw1.title("About Project")

    canvas = Canvas(smw1, width=1500, height=750, bg="SpringGreen2")
    canvas.create_text(500, 100, text="Transport packer and movers Its python GUI Desktop application using Tkinter "
                                      "\nfor GUI Interface and MySQL database as backend it's a desktop application "
                                      "\nsingle user which has two modules admin, user Admin module: Admin allowed to "
                                      "\ncreate new user, change its and change admin password itself, admin role to "
                                      "\nset fare of transport goods, admin also checks booking details and various "
                                      "\nreports on bookingdaily, monthly and yearly User module: User are allowed to "
                                      "\naccept the booking, check a booking, modify booking, search booking,update, "
                                      "\nor cancel booking also allowed to check fare details", fill="black",
                       font='Helvetica 15 bold')
    canvas.pack()
    smw1.mainloop()
