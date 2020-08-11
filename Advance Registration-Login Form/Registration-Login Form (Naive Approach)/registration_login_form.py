# Importing Tkinter
from tkinter import *
from tkinter import messagebox
import os
from time import sleep

# Creating Driver Function
def DriverFunction():
    global root_main_screen
    root_main_screen = Tk()                                         # creating object of Tk() class to start the Tkinter GUI Window
    root_main_screen.title('Main')                                  # Giving the title to GUI Window
    root_main_screen.geometry('300x180')                            # setting the geometry of GUI Window
    root_main_screen.minsize(300, 180)                              # setting the minsize of GUI Window
    root_main_screen.maxsize(300, 180)                              # setting the maxsize of GUI Window
    Label(text = 'Choose', font = 'comicsansms 10 bold', bg = '#f9ad5a', fg = '#3d2c32', width = 400, height = 2).pack()
    Label(text = '').pack()
    # Creating Driver Buttons
    Button(text = 'Register', font = 'comicsansms 8 bold', bg = '#101820', fg = '#f2aa4c', borderwidth = 5, relief = 'sunken', width = 30, command = Register).pack()
    Button(text = 'Login', font = 'comicsansms 8 bold', bg = '#101820', fg = '#f2aa4c', borderwidth = 5, relief = 'sunken', width = 30, command = Login).pack(pady = 12)
    root_main_screen.mainloop()                                     # Holding the GUI Window in infinite loop


# Creating Function for Register Operation
def Register():
    global root_register_screen
    root_register_screen = Toplevel(root_main_screen)
    root_register_screen.title('Registration Page')
    root_register_screen.geometry('500x500')
    root_register_screen.minsize(500, 500)
    root_register_screen.maxsize(500, 500)
    Label(root_register_screen, text = 'Register', font = 'comicsansms 10 bold', bg = '#f9ad5a', fg = '#3d2c32', width = 500, height = 2).pack()

    global name
    global registration_num
    global username
    global password
    global email
    global contact

    name = StringVar()
    registration_num = StringVar()
    username = StringVar()
    password = StringVar()
    email = StringVar()
    contact = StringVar()

    # Creating Entry Fields

    Label(root_register_screen, text = '').pack()
    Label(root_register_screen, text = 'Enter Name').pack()
    Entry(root_register_screen, textvariable = name).pack()

    Label(root_register_screen, text = '').pack()
    Label(root_register_screen, text = 'Enter Registration Number').pack()
    Entry(root_register_screen, textvariable = registration_num).pack()

    Label(root_register_screen, text = '').pack()
    Label(root_register_screen, text = 'Enter Username').pack()
    Entry(root_register_screen, textvariable = username).pack()

    Label(root_register_screen, text = '').pack()
    Label(root_register_screen, text = 'Enter Password').pack()
    Entry(root_register_screen, textvariable = password, show = '*').pack()

    Label(root_register_screen, text = '').pack()
    Label(root_register_screen, text = 'Enter Email').pack()
    Entry(root_register_screen, textvariable = email).pack()

    Label(root_register_screen, text = '').pack()
    Label(root_register_screen, text = 'Enter Contact Number').pack()
    Entry(root_register_screen, textvariable = contact).pack()

    Label(root_register_screen, text='').pack()
    # Creating Button
    Button(root_register_screen, text = 'Register', font = 'comicsansms 8 bold', bg = '#101820', fg = '#f2aa4c', borderwidth = 5, relief = 'sunken', width = 20, command = RegisterDetails).pack()


# Creating Function to Store Data
def RegisterDetails():
    if os.path.isfile(username.get()):
        messagebox.showwarning('Username Exists', 'You are already Registered, Please Login')
        sleep(1)
        quit()
    else:
        # Using File Handling to store User Input Data
        file = open(username.get(), 'w')
        file.write(name.get() + '\n')
        file.write(registration_num.get() + '\n')
        file.write(username.get() + '\n')
        file.write(password.get() + '\n')
        file.write(email.get() + '\n')
        file.write(contact.get())
        file.close()
        Label(root_register_screen, text="Registration Success", fg="green", font='comicsansms 8 bold').pack()
        sleep(2)
        Login()
    name.set('')
    registration_num.set('')
    username.set('')
    password.set('')
    email.set('')
    contact.set('')


# Creating Function for login Operation
def Login():
    global root_login_screen
    root_login_screen = Toplevel(root_main_screen)
    root_login_screen.title('Login')
    root_login_screen.geometry('500x300')
    root_login_screen.minsize(500, 300)
    root_login_screen.maxsize(500, 300)
    Label(root_login_screen, text = 'Login', font = 'comicsansms 10 bold', bg = '#f9ad5a', fg = '#3d2c32', width = 500,
          height = 2).pack()

    global username_login
    global password_login

    username_login = StringVar()
    password_login = StringVar()

    # Creating Entry Fields

    Label(root_login_screen, text='').pack()
    Label(root_login_screen, text='Enter Username').pack()
    Entry(root_login_screen, textvariable=username_login).pack()

    Label(root_login_screen, text='').pack()
    Label(root_login_screen, text='Enter Password').pack()
    Entry(root_login_screen, textvariable=password_login, show='*').pack()

    Label(root_login_screen, text='').pack()
    # Creating Button
    Button(root_login_screen, text='Login', font='comicsansms 8 bold', bg='#101820', fg='#f2aa4c', borderwidth=5,
           relief='sunken', width=20, command=LoginDetails).pack()


# Creating function for Login Credential Check
def LoginDetails():
    if os.path.isfile(username_login.get()):
        f = open(username_login.get(), 'r')
        user_data = f.read().splitlines()
        if password_login.get() in user_data:
            Label(root_login_screen, text="Login Success", fg="green", font='comicsansms 8 bold').pack()
            sleep(2)
            AfterLogin()
        else:
            messagebox.showinfo('Login Failed', 'Password Incorrect')
            sleep(1)
            quit()
    else:
        messagebox.showinfo('Login Failed', 'Username Doesn\'t Exist')
        sleep(1)
        quit()

    username_login.set('')
    password_login.set('')


# Function for Future Ideas and References
def AfterLogin():
    print('Success')


# Calling Driver Function
if __name__ == '__main__':
    DriverFunction()
