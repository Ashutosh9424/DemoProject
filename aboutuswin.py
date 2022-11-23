# from tkinter import *
# from tkinter import messagebox
# import mysql.connector
#
#
# def aboutususerwin():
#     smw1 = Tk()
#     smw1.geometry("1000x500")
#     smw1.title("About Us")
#
#     canvas = Canvas(smw1, width=1500, height=750, bg="SpringGreen2")
#     canvas.create_text(500, 100, text="Transport packer and movers Its python GUI Desktop application using Tkinter "
#                                       "\nfor GUI Interface and MySQL database as backend it's a desktop application "
#                                       "\nsingle user which has two modules admin, user Admin module: Admin "
#                                       "allowed to "
#                                       "\ncreate new user, change its and change admin password itself, admin role to "
#                                       "\nset fare of transport goods, admin also checks booking details and various "
#                                       "\nreports on bookingdaily, monthly and yearly User module: User are "
#                                       "allowed to "
#                                       "\naccept the booking, check a booking, modify booking, search booking,update, "
#                                       "\nor cancel booking also allowed to check fare details", fill="black",
#                        font='Helvetica 15 bold')
#     canvas.pack()
#     smw1.mainloop()


from tkinter import *

def aboutususerwin():

    au=Tk()
    au.title("About us")
    au.geometry("1368x750")
    au.config(bg="white")
    lb = Label(au, text="Developed by-", bg="yellow", fg="red", font=("elephant", 35))
    lb1 = Label(au, text="Ashutosh Pandey", bg="salmon", fg="white", font=("elephant", 40))
    lb2 = Label(au, text="Guided by-", bg="yellow", fg="red", font=("elephant", 35))
    lb3 = Label(au, text="Sushil patel sir", bg="salmon", fg="white", font=("elephant", 40))


    lb.place(x=250, y=10)
    lb1.place(x=170, y=100)
    lb2.place(x=250, y=200)
    lb3.place(x=170, y=290)

    au.mainloop()
