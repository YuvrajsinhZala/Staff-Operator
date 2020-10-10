import sqlite3
import mttkinter
import tkinter
import tkinter.messagebox as tk
from tkinter.font import Font
from easygui import *
from tkinter import *
from turtle import *
import random

conn = sqlite3.connect('Yuvraj-leaveDb.db')
cur = conn.cursor()


def AdminLogin():
    message = "Enter Username and Password"
    title = "Admin Login"
    fieldnames = ["Username", "Password"]
    field = []
    field = multpasswordbox(message, title, fieldnames)
    if field[0] == 'admin' and field[1] == 'admin':
        tkinter.messagebox.showinfo("Admin Login", "Login Successfully")
        adminwindow()
    else:
        tk.showerror("Error info", "Incorrect username or password")


def EmployeeLogin():
    message = "Enter Employee ID and Password"
    title = "Employee Login"
    fieldnames = ["Employee ID", "Password"]
    field = []
    field = multpasswordbox(message, title, fieldnames)

    for row in conn.execute('SELECT * FROM employee'):
        if field[0] == row[0] and field[1] == row[3]:
            global login
            login = field[0]
            f = 1
            print("Success")
            tkinter.messagebox.showinfo("Employee Login", "Login Successfully")
            EmployeeLoginWindow()
            break
    if not f:
        print("Invalid")
        tk.showerror("Error info", "Incorrect employee id or password")

def Employeelogout():
    global login
    login = -1
    LoginWindow.destroy()


def EmployeeLeaveStatus():
    global leaveStatus
    leaveStatus = []
    for i in conn.execute('SELECT * FROM status where employee_id=?', login):
        leaveStatus = i

    WindowStatus()


def EmployeeAllStatus():
    allStatus = Toplevel()
    txt = Text(allStatus)
    for i in conn.execute('SELECT * FROM status where employee_id=?', login):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')

    txt.pack()


def EmployeeInformationWindow():
    employeeInformation = Toplevel()
    txt = Text(employeeInformation)
     
    for i in conn.execute('SELECT employee_id,Name,ContactNumber FROM employee where employee_id=?', login):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')

    txt.pack()


def EmployeeAllInformationWindow():
    allEmployeeInformation = Toplevel()
    txt = Text(allEmployeeInformation)
    for i in conn.execute('SELECT employee_id,Name,ContactNumber FROM employee'):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')

    txt.pack()


def balance():
    global login
    check = (login,)
    global balanced
    balanced = []
    for i in conn.execute('SELECT * FROM balance WHERE employee_id = ?', check):
        balanced = i

    WindowBalance()


def LeaveApproval():
    exit;
    
def leavelist():
    leavelistwindow = Toplevel()
    txt = Text(leavelistwindow)
    for i in conn.execute('SELECT * FROM status'):
        txt.insert(INSERT, i)
        txt.insert(INSERT, '\n')

    txt.pack()


def registration():
    message = "Enter Details of Employee"
    title = "Registration"
    fieldNames = ["Employee ID", "Name", "Contact Number", "Password"]
    fieldValues = []
    fieldValues = multpasswordbox(message, title, fieldNames)
    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])

        if errmsg == "": break


        fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)
    conn.execute("INSERT INTO employee(employee_id,Name,ContactNumber,Password) VALUES (?,?,?,?)",
                 (fieldValues[0], fieldValues[1], fieldValues[2], fieldValues[3]))
    conn.execute("INSERT INTO balance(employee_id,sickleave,maternityleave,emergencyleave) VALUES (?,?,?,?)", (fieldValues[0], 12, 12, 50))
    conn.commit()


def EmployeeLoginWindow():
    # employee login window after successful login
    global LoginWindow
    LoginWindow = Toplevel()
    LoginWindow.wm_attributes('-fullscreen', '1')
    Background_Label = Label(LoginWindow, image=filename)
    Background_Label.place(x=0, y=0, relwidth=1, relheight=1)

    informationEmployee = Button(LoginWindow, text='Employee information', command=EmployeeInformationWindow, bd=12, relief=GROOVE, fg="green", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    informationEmployee['font'] = BtnFont
    informationEmployee.pack(fill=X)

    submit = Button(LoginWindow, text='Submit Leave', command=apply, bd=12, relief=GROOVE, fg="white", bg="#ff0003",
                      font=("Calibri", 36, "bold"), pady=3)
    submit['font'] = BtnFont
    submit.pack(fill=X)

    LeaveBalance = Button(LoginWindow, text='Leave Balance', command=balance, bd=12, relief=GROOVE, fg="white", bg="#ff0003",
                      font=("Calibri", 36, "bold"), pady=3)
    LeaveBalance['font'] = BtnFont
    LeaveBalance.pack(fill=X)

    LeaveApplicationStatus = Button(LoginWindow, text='Last leave status', command=EmployeeLeaveStatus, bd=12, relief=GROOVE, fg="white", bg="#ff0003",
                      font=("Calibri", 36, "bold"), pady=3)
    LeaveApplicationStatus['font'] = BtnFont
    LeaveApplicationStatus.pack(fill=X)

    AllLeaveStatus = Button(LoginWindow, text='All leave status', command=EmployeeAllStatus, bd=12, relief=GROOVE, fg="white", bg="#ff0003",
                      font=("Calibri", 36, "bold"), pady=3)
    AllLeaveStatus['font'] = BtnFont
    AllLeaveStatus.pack(fill=X)


    LogoutBtn = Button(LoginWindow, text='Logout', bd=12, relief=GROOVE, fg="red", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3, command=Employeelogout)
    LogoutBtn['font'] = BtnFont
    LogoutBtn.pack(fill=X)

    informationEmployee.pack()
    LogoutBtn.pack()
    ExitBtn.pack()



def adminwindow():
    adminmainwindow = Toplevel()
    adminmainwindow.wm_attributes('-fullscreen', '1')
    Background_Label = Label(adminmainwindow, image=filename)

    Background_Label.place(x=0, y=0, relwidth=1, relheight=1)
    informationEmployee = Button(adminmainwindow, text='All Employee information', command=EmployeeAllInformationWindow, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
    informationEmployee['font'] = BtnFont
    informationEmployee.pack(fill=X)



    LeaveListButton = Button(adminmainwindow, text='Leave approval list', command=leavelist, bd=12, relief=GROOVE, fg="white", bg="#ff0003",
                      font=("Calibri", 36, "bold"), pady=3)
    LeaveListButton['font'] = BtnFont
    LeaveListButton.pack(fill=X)

    ApprovalButton = Button(adminmainwindow, text='Approve leave', command=LeaveApproval, bd=12, relief=GROOVE, fg="white", bg="#ff0003",
                      font=("Calibri", 36, "bold"), pady=3)
    ApprovalButton['font'] = BtnFont
    ApprovalButton.pack(fill=X)

    LogoutBtn = Button(adminmainwindow, text='Logout', command=adminmainwindow.destroy, bd=12, relief=GROOVE, fg="red",
                     bg="#ffffb3",
                     font=("Calibri", 36, "bold"), pady=3)
    LogoutBtn['font'] = BtnFont
    LogoutBtn.pack(fill=X)

    informationEmployee.pack()
    ExitBtn.pack()


root = Tk()
root.wm_attributes('-fullscreen', '1')
root.title("Staff Operator - YZ")
root.iconbitmap(default='leavelogo.ico')
filename = PhotoImage(file="background.gif")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
BtnFont = Font(family='Calibri(Body)', size=20)
MainLabel = Label(root, text="Staff Operator - YZ", bd=12, relief=GROOVE, fg="White", bg="green",
                      font=("Calibri", 36, "bold"), pady=3)
MainLabel.pack(fill=X)
im = PhotoImage(file='login.gif')

AdminLgnBtn = Button(root, text='Admin login',  bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3, command=AdminLogin)
AdminLgnBtn['font'] = BtnFont
AdminLgnBtn.pack(fill=X)


LoginBtn = Button(root, text='Employee login', bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3, command=EmployeeLogin)
LoginBtn['font'] = BtnFont
LoginBtn.pack(fill=X)


EmployeeRegistration = Button(root, text='Employee registration', command=registration, bd=12, relief=GROOVE, fg="blue", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
EmployeeRegistration['font'] = BtnFont
EmployeeRegistration.pack(fill=X)

ExitBtn = Button(root, text='Exit', command=root.destroy, bd=12, relief=GROOVE, fg="red", bg="#ffffb3",
                      font=("Calibri", 36, "bold"), pady=3)
ExitBtn['font'] = BtnFont
ExitBtn.pack(fill=X)
MainLabel.pack()
AdminLgnBtn.pack()
LoginBtn.pack()
EmployeeRegistration.pack()
ExitBtn.pack()


root.mainloop()
