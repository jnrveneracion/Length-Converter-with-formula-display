#import modules
from ast import For, Global
from logging import root
from secrets import choice
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
from turtle import position, xcor
import webbrowser
from PIL import Image, ImageTk
import os

#Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel()
    login_success_screen.geometry("500x560+700+200")

    img = ImageTk.PhotoImage(Image.open("authors.png"))
    label = Label(login_success_screen, image= img)
    label.pack()

    Label(login_success_screen, fg="green", text="Login Success").pack()  
    Button(login_success_screen, text="Proceed", command=delete_login_success).pack()

    root = Toplevel()
    frame = tk.Frame(root, width=500, height=600)

    image1 = Image.open("headimg.png")
    test = ImageTk.PhotoImage(image1)

    label1 = tk.Label(frame, image=test, width=500)
    label1.image = test

    toplabel = tk.Label(frame, text='From:                     To:', fg='black', font=('courier', 17, BOLD), width=35,
                        height=1, )

    entry_n1 = tk.Entry(frame, font=('courier', 16), width=20)

    entry_result = tk.Entry(frame, font=('courier', 16), width=20, justify=CENTER)

    options1 = ['Select Unit', '[km]Kilometer', '[m]Meter', '[cm]Centimeter', '[mm]Millimeter', '[μm]Micrometer',
                '[nm]Nanometer', '[mi]Mile', '[yd]Yard', '[ft]Foot', '[in]Inch', '[nm]Nautical Mile']
    selected1 = StringVar(frame)
    selected1.set(options1[0])
    combobox1 = ttk.Combobox(frame, textvariable=selected1, values=options1, font=('courier', 14), width=19, justify=CENTER,
                            state='readonly')

    btn1 = tk.Button(frame, text='Convert', fg='black', font=('courier', 15), width=6, height=1)
    btn2 = tk.Button(frame, text='Logout and Close', fg='black', font=('courier', 15), command=exit, width=15, height=1)

    options2 = ['Select Unit', '[km]Kilometer', '[m]Meter', '[cm]Centimeter', '[mm]Millimeter', '[μm]Micrometer',
                '[nm]Nanometer', '[mi]Mile', '[yd]Yard', '[ft]Foot', '[in]Inch', '[nm]Nautical Mile']
    selected = StringVar(frame)
    selected.set(options2[0])
    combobox2 = ttk.Combobox(frame, textvariable=selected, values=options2, font=('courier', 14), width=19, justify=CENTER,
                            state='readonly')

    label = tk.Label(frame, text='=', fg='black', font=('courier', 23), width=2, height=1)

    direction = tk.Message(frame, text='''
What is Length Conversion?
Length conversion is the procedure of converting the units of length with the help of the correct conversion factor.
We deal with measurements every day and converting these units to the required unit involves the process of
multiplication or division.
\n
How to use:
Step 1: Choose the length unit you want to convert from.
Step 2: Input an integer that you want to convert.
Step 3: Choose the length unit you want to convert to.
Step 4: Click the Convert button and see the conversion
        result and formula applied.


Documentation Link: ''', fg='black', font=('courier', 12), width=420)

    Formula = tk.Message(frame, text='Formula: ', fg='white', bg='orange', font=('courier', 12), width=300)
    Formulamess = tk.Entry(frame, font=('courier', 12), width=45, justify=LEFT)

    documentation = tk.Label(frame, text='Conversion of Length Documentation', font=('courier', 12), fg="blue")
    documentation.bind("<Button-1>", lambda e: callback("https://bit.ly/3oBWptV"))


    def callback(url):
        webbrowser.open_new_tab(url)

    def calculate():
        try: 
            num1 = float(entry_n1.get())
            opt1 = combobox1.get()
            opt2 = combobox2.get()
            if opt1 == '[km]Kilometer':
                choice1 = 1
            elif opt1 == '[m]Meter':
                choice1 = 2
            elif opt1 == '[cm]Centimeter':
                choice1 = 3
            elif opt1 == '[mm]Millimeter':
                choice1 = 4
            elif opt1 == '[in]Inch':
                choice1 = 10
            elif opt1 == '[nm]Nautical Mile':
                choice1 = 11
            elif opt1 == '[μm]Micrometer':
                choice1 = 5
            elif opt1 == 'Select Unit':
                choice1 = 12
            elif opt1 == '[mi]Mile':
                choice1 = 7
            elif opt1 == '[yd]Yard':
                choice1 = 8
            elif opt1 == '[ft]Foot':
                choice1 = 9
            elif opt1 == '[nm]Nanometer':
                choice1 = 6    
            else:
                choice1 = 14

            if opt2 == '[km]Kilometer':
                choice2 = 1
            elif opt2 == '[m]Meter':
                choice2 = 2
            elif opt2 == '[cm]Centimeter':
                choice2 = 3
            elif opt2 == '[mm]Millimeter':
                choice2 = 4
            elif opt2 == '[μm]Micrometer':
                choice2 = 5
            elif opt2 == '[in]Inch':
                choice2 = 10
            elif opt2 == '[nm]Nautical Mile':
                choice2 = 11
            elif opt2 == 'Select Unit':
                choice2 = 12
            elif opt2 == '[mi]Mile':
                choice2 = 7
            elif opt2 == '[yd]Yard':
                choice2 = 8
            elif opt2 == '[ft]Foot':
                choice2 = 9
            elif opt2 == '[nm]Nanometer':
                choice2 = 6
            else:
                choice2 = 14

            cal(choice1, choice2, num1)
        except NameError:
            txt = "Namerror"
            
        except TypeError:
            txt = "Typerror"
            result = 0

        except ValueError:
            txt = "Invalid Input. Please enter a number."    
            result = 0
        gain(txt, result)    
        

    def cal(choice1, choice2, num1):
        # fromKilometer
        if choice1 == 1:
            if choice2 == 1:
                result = num1
                txt = "Kilometer to Kilometer.. :)"
            elif choice2 == 2:
                result = num1 * 1000
                txt = "multiply the length value by 1000"
            elif choice2 == 3:
                result = num1 * 100000
                txt = "multiply the length value by 100000"
            elif choice2 == 4:
                result = num1 * 1e+6
                txt = "multiply the length value by 1e+6"
            elif choice2 == 5:
                result = num1 * 1e+9
                txt = "multiply the length value by 1e+9"
            elif choice2 == 6:
                result = num1 * 1e+12
                txt = "multiply the length value by 1e+12"
            elif choice2 == 7:
                result = num1 / 1.609
                txt = "Divide the length value from 1.609"
            elif choice2 == 8:
                result = num1 * 1094
                txt = "multiply the length value by 1094"
            elif choice2 == 9:
                result = num1 * 3281
                txt = "multiply the length value by 3281"
            elif choice2 == 10:
                result = num1 * 39370
                txt = "multiply the length value by 39370"
            elif choice2 == 11:
                result = num1 / 1.852
                txt = "multiply the length value by 1.852"
            if choice2 == 12:
                result = 0
                txt = "Please Select Length Unit"

                # fromMeter
        elif choice1 == 2:
            if choice2 == 1:
                result = num1 / 1000
                txt = "divide the length value by 1000"
            elif choice2 == 2:
                result = num1
                txt = "Meter to Meter.. :)"
            elif choice2 == 3:
                result = num1 * 100
                txt = "multiply the length value by 100"
            elif choice2 == 4:
                result = num1 * 1000
                txt = "multiply the length value by 1000"
            elif choice2 == 5:
                result = num1 * 1e+6
                txt = "multiply the length value by 1e+6"
            elif choice2 == 6:
                result = num1 * 1e+9
                txt = "multiply the length value by 1e+9"
            elif choice2 == 7:
                result = num1 / 1609
                txt = "divide the length value by 1609"
            elif choice2 == 8:
                result = num1 * 1.094
                txt = "multiply the length value by 1.094"
            elif choice2 == 9:
                result = num1 * 3.281
                txt = "multiply the length value by 3.281"
            elif choice2 == 10:
                result = num1 * 39.37
                txt = "multiply the length value by 39.37"
            elif choice2 == 11:
                result = num1 / 1852
                txt = "divide the length value by 1852"
            if choice2 == 12:
                result = 0
                txt = "Please Select Length Unit"

                # fromCentimeter
        if choice1 == 3:
            if choice2 == 1:
                result = num1 / 100000
                txt = "divide the length value by 100000"
            elif choice2 == 2:
                result = num1 / 100
                txt = "divide the length value by 100"
            elif choice2 == 3:
                result = num1
                txt = "Centimeter to Centimeter.. :)"
            elif choice2 == 4:
                result = num1 * 10
                txt = "multiply the length value by 10"
            elif choice2 == 5:
                result = num1 * 10000
                txt = "multiply the length value by 10000"
            elif choice2 == 6:
                result = num1 * 1e+7
                txt = "multiply the length value by 1e+7"
            elif choice2 == 7:
                result = num1 / 160900
                txt = "divide the length value by 160900"
            elif choice2 == 8:
                result = num1 / 91.44
                txt = "divide the length value by 91.44"
            elif choice2 == 9:
                result = num1 / 30.48
                txt = "divide the length value by 30.48"
            elif choice2 == 10:
                result = num1 / 2.54
                txt = "divide the length value by 2.54"
            elif choice2 == 11:
                result = num1 / 185200
                txt = "divide the length value by 185200"
            if choice2 == 12:
                result = 0
                txt = "Please Select Length Unit"

                # fromMillimeter
        elif choice1 == 4:
            if choice2 == 1:
                result = num1 / 1e+6
                txt = "divide the length value by 1e+6"
            elif choice2 == 2:
                result = num1 / 1000
                txt = "divide the length value by 1000"
            elif choice2 == 3:
                result = num1 / 10
                txt = "divide the length value by 10"
            elif choice2 == 4:
                result = num1
                txt = "Millimeter to Millimeter.. :)"
            elif choice2 == 5:
                result = num1 * 1000
                txt = "multiply the length value by 1000"
            elif choice2 == 6:
                result = num1 * 1e+6
                txt = "multiply the length value by 1e+6"
            elif choice2 == 7:
                result = num1 / 1.609e+6
                txt = "divide the length value by 1.609e+6"
            elif choice2 == 8:
                result = num1 / 914.4
                txt = "divide the length value by 914.4"
            elif choice2 == 9:
                result = num1 / 304.8
                txt = "divide the length value by 304.8"
            elif choice2 == 10:
                result = num1 / 25.4
                txt = "divide the length value by 25.4"
            elif choice2 == 11:
                result = num1 / 1.852e+6
                txt = "divide the length value by 1.852e+6"
            if choice2 == 12:
                result = 0
                txt = "Please Select Length Unit"

                # fromMicrometer
        elif choice1 == 5:
            if choice2 == 1:
                result = num1 / 1e+9  
                txt = "divide the length value by 1e+9"
            elif choice2 == 2:
                result = num1 / 1e+6 
                txt = "divide the length value by 1e+6"
            elif choice2 == 3:
                result = num1 / 10000
                txt = "divide the length value by 10000"
            elif choice2 == 4:
                result = num1 / 1000
                txt = "divide the length value by 1000"
            elif choice2 == 5:
                result = num1
                txt = "Micrometer to Micrometer.. :)"
            elif choice2 == 6:
                result = num1 * 1000
                txt = "multiply the length value by 1000"
            elif choice2 == 7:
                result = num1 / 1.609e+9
                txt = "divide the length value by 1.609e+9"
            elif choice2 == 8:
                result = num1 / 914400
                txt = "divide the length value by 914400"
            elif choice2 == 9:
                result = num1 / 304800
                txt = "divide the length value by 304800"
            elif choice2 == 10:
                result = num1 / 25400
                txt = "divide the length value by 25400"
            elif choice2 == 11:
                result = num1 / 1.852e+9
                txt = "divide the length value by 1.852e+9"
            if choice2 == 12:
                result = 0
                txt = "Please Select Length Unit"

        elif choice1 == 12:
            if (choice2 == 12) or (choice2 == 1) or (choice2 == 2) or (choice2 == 3) or (choice2 == 4) or (choice2 == 5) or (choice2 == 6) or (choice2 == 7) or (choice2 == 8) or (choice2 == 9) or (choice2 == 10) or (choice2 == 11):
                result = 0
                txt = "Please Select Length Unit"

        # fromNanometer
        elif choice1 == 6:
            if choice2 == 1:
                result = num1 / 1e+12
                txt = "divide the length value by 1e+12"
            elif choice2 == 2:
                result = num1 / 1e+9
                txt = "divide the length value by 1e+9"
            elif choice2 == 3:
                result = num1 / 1e+7
                txt = "divide the length value by 1e+7"
            elif choice2 == 4:
                result = num1 / 1e+6
                txt = "divide the length value by 1e+6"
            elif choice2 == 5:
                result = num1 / 1000
                txt = "divide the length value by 1000"
            elif choice2 == 6:
                result = num1
                txt = "Nanometer to Nanometer.. :)"
            elif choice2 == 7:
                result = num1 / 1.609e+12
                txt = "divide the length value by 1.609e+12"
            elif choice2 == 8:
                result = num1 / 9.144e+8
                txt = "divide the length value by 9.144e+8"
            elif choice2 == 9:
                result = num1 / 3.048e+8
                txt = "divide the length value by 3.048e+8"
            elif choice2 == 10:
                result = num1 / 2.54e+7
                txt = "divide the length value by 2.54e+7"
            elif choice2 == 11:
                result = num1 / 1.852e+12
                txt = "divide the length value by 1.852e+12"
            if choice2 == 12:
                result = 0
                txt = "Please Select Length Unit"

        # fromMile
        elif choice1 == 7:
            if choice2 == 1:
                result = num1 * 1.609
                txt = "multiply the length value by 1.609"
            elif choice2 == 2:
                result = num1 * 1609
                txt = "multiply the length value by 1609"
            elif choice2 == 3:
                result = num1 * 160900
                txt = "multiply the length value by 160900"
            elif choice2 == 4:
                result = num1 * 1.609e+6
                txt = "multiply the length value by 1.609e+6"
            elif choice2 == 5:
                result = num1 * 1.609e+9
                txt = "multiply the length value by 1.609e+9"
            elif choice2 == 6:
                result = num1 * 1.609e+12
                txt = "multiply the length value by 1.609e+12"
            elif choice2 == 7:
                result = num1
                txt = "Mile to Mile.. :)"
            elif choice2 == 8:
                result = num1 * 1760
                txt = "multiply the length value by 1760"
            elif choice2 == 9:
                result = num1 * 5280
                txt = "multiply the length value by 5280"
            elif choice2 == 10:
                result = num1 * 63360
                txt = "multiply the length value by 63360"
            elif choice2 == 11:
                result = num1 / 1.151
                txt = "divide the length value by 1.151"
            if choice2 == 12:
                result = 0
                txt = "Please Select Length Unit"

                # fromYard
        elif choice1 == 8:
            if choice2 == 1:
                result = num1 / 1094
                txt = "divide the length value by 1094"
            elif choice2 == 2:
                result = num1 / 1.094
                txt = "divide the length value by 1.094"
            elif choice2 == 3:
                result = num1 * 91.44
                txt = "multiply the length value by 91.44"
            elif choice2 == 4:
                result = num1 * 914.4
                txt = "multiply the length value by 914.4"
            elif choice2 == 5:
                result = num1 * 914400
                txt = "multiply the length value by 914400"
            elif choice2 == 6:
                result = num1 * 9.144e+8
                txt = "multiply the length value by 9.144e+8"
            elif choice2 == 7:
                result = num1 / 1760
                txt = "divide the length value by 1760"
            elif choice2 == 8:
                result = num1
                txt = "Yard to Yard.. :)"
            elif choice2 == 9:
                result = num1 * 3
                txt = "multiply the length value by 3"
            elif choice2 == 10:
                result = num1 * 36
                txt = "multiply the length value by 36"
            elif choice2 == 11:
                result = num1 / 2025
                txt = "divide the length value by 2025"
            if choice2 == 12:
                result = 0
                txt = "Please Select Length Unit"

                # frmFoot
        elif choice1 == 9:
            if choice2 == 1:
                result = num1 / 3281
                txt = "divide the length value by 3281"
            elif choice2 == 2:
                result = num1 / 3.281
                txt = "divide the length value by 3.281"
            elif choice2 == 3:
                result = num1 * 30.48
                txt = "multiply the length value by 30.48"
            elif choice2 == 4:
                result = num1 * 304.8
                txt = "multiply the length value by 304.8"
            elif choice2 == 5:
                result = num1 * 304800
                txt = "multiply the length value by 304800"
            elif choice2 == 6:
                result = num1 * 3.048e+8
                txt = "multiply the length value by 3.048e+8"
            elif choice2 == 7:
                result = num1 / 5280
                txt = "divide the length value by 5280"
            elif choice2 == 8:
                result = num1 / 3
                txt = "divide the length value by 3"
            elif choice2 == 9:
                result = num1
                txt = "Foot to Foot.. :)"
            elif choice2 == 10:
                result = num1 * 12
                txt = "multiply the length value by 12"
            elif choice2 == 11:
                result = num1 / 6076
                txt = "divide the length value by 6076"
            if choice2 == 12:
                result = 0
                txt = "Please Select Length Unit"

        # fromInch
        elif choice1 == 10:
            if choice2 == 1:
                result = num1 / 39370
                txt = "divide the length value by 39370"
            elif choice2 == 2:
                result = num1 / 39.37
                txt = "divide the length value by 39.37"
            elif choice2 == 3:
                result = num1 * 2.54
                txt = "multiply the length value by 2.54"
            elif choice2 == 4:
                result = num1 * 25.4
                txt = "multiply the length value by 25.4"
            elif choice2 == 5:
                result = num1 * 25400
                txt = "multiply the length value by 25400"
            elif choice2 == 6:
                result = num1 * 2.54e+7
                txt = "multiply the length value by 2.54e+7"
            elif choice2 == 7:
                result = num1 / 63360
                txt = "divide the length value by 63360"
            elif choice2 == 8:
                result = num1 / 36
                txt = "divide the length value by 36"
            elif choice2 == 9:
                result = num1 / 12
                txt = "divide the length value by 12"
            elif choice2 == 10:
                result = num1
                txt = "Inch to Inch.. :)"
            elif choice2 == 11:
                result = num1 / 72910
                txt = "divide the length value by 72910"
            if choice2 == 12:
                result = 0
                txt = "Please Select Length Unit"

                # fromNatuMile
        elif choice1 == 11:
            if choice2 == 1:
                result = num1 * 1.852
                txt = "multiply the length value by 1.852"
            elif choice2 == 2:
                result = num1 * 1852
                txt = "multiply the length value by 1852"
            elif choice2 == 3:
                result = num1 * 185200
                txt = "multiply the length value by 185200"
            elif choice2 == 4:
                result = num1 * 1.852e+6
                txt = "multiply the length value by 1.852e+6"
            elif choice2 == 5:
                result = num1 * 1.852e+9
                txt = "multiply the length value by 1.852e+9"
            elif choice2 == 6:
                result = num1 * 1.852e+12
                txt = "multiply the length value by 1.852e+12"
            elif choice2 == 7:
                result = num1 * 1.151
                txt = "multiply the length value by 1.151"
            elif choice2 == 8:
                result = num1 * 2025
                txt = "multiply the length value by 2025"
            elif choice2 == 9:
                result = num1 * 6076
                txt = "multiply the length value by 6076"
            elif choice2 == 10:
                result = num1 * 72910
                txt = "multiply the length value by 72910"
            elif choice2 == 11:
                result = num1
                txt = "Nautical mile to Nautical mile .. :)"
            if choice2 == 12:
                result = 0
                txt = "Please Select Length Unit"
        gain(txt, result)


    def gain(txt, result):
        entry_result.delete(0, END)
        Formulamess.delete(0, END)
        Formulamess.insert(0, txt)
        result = round(result, 12)
        entry_result.insert(0, result)


    btn1['command'] = calculate
    frame.pack()
    root.resizable(False, False)
    label1.place(x= -5, y= 0)
    toplabel.place(x=45, y=125)
    entry_n1.place(x=20, y=150)
    entry_result.place(x=270, y=150)
    combobox1.place(x=40, y=190)
    combobox2.place(x=290, y=190)
    label.place(x=230, y=150)
    btn1.place(x=204, y=230)
    btn2.place(x=320, y=560)

    Formula.place(x=50, y=270)
    Formulamess.place(x=120, y=267)
    documentation.place(x=180, y=530)

    direction.place(x=35, y=310)

    root.mainloop()
 
 
# Designing window for registration
def register():
    main_screen.state(newstate='iconic')
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("380x250+700+200")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="").pack()
    Label(register_screen, text="Enter details below to register", font=("courier", 17, BOLD)).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
    Button(register_screen, text="Login", width=10, height=1, bg="blue", command = login).pack()
    
# Designing window for login 
 
def login():
    
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("380x250+700+200")
    Label(login_screen, text="").pack()
    Label(login_screen, text="Enter details below to login", font=("courier", 17, BOLD)).pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("courier", 12)).pack()
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

            
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Error!")
    password_not_recog_screen.geometry("150x60+700+200")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Error!")
    user_not_found_screen.geometry("150x60+700+200")


    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.state(newstate='iconic')
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def exit():
    main_screen.destroy() 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("380x250+700+200")
    main_screen.title("Length Converter")
    Label(text="").pack()
    Label(text="Conversion of Length System" , width="60", height="2", font=("courier", 17, BOLD)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="25", command = login, font=("courier", 13)).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="25", command= register, font=("courier", 13)).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()