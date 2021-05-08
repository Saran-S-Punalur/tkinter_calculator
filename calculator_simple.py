"""
Simple python math solving GUI using NumPy and Tkinter
https://github.com/Saran-S-Punalur/

Saran S 

07/05/2021  07:51 pm

"""

#pyinstaller --onefile -w calculator_simple.py

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo


frame1 = tk.Tk()
frame1.geometry("1150x900") 
frame1.resizable(0, 0)                 #make unresizable
frame1.title("NumPer")
frame1.configure(bg = 'PaleGreen3')
frame1.iconbitmap("F:/PythonProjects/icons/calcu.ico")
#===========================================FUNCTIONS=======================================
#BASIC
def c_one():
    bas_ent.insert("end", '1')
def c_two():
    bas_ent.insert("end", '2')
def c_three():
    bas_ent.insert("end", '3')
def c_four():
    bas_ent.insert("end", '4')
def c_five():
    bas_ent.insert("end", '5')
def c_six():
    bas_ent.insert("end", '6')
def c_seven():
    bas_ent.insert("end", '7')
def c_eight():
    bas_ent.insert("end", '8')
def c_nine():
    bas_ent.insert("end", '9')
def c_zero():
    bas_ent.insert("end", '0')
def c_dot():
    bas_ent.insert("end", '.')
def c_prod():
    bas_ent.insert("end", '*')
def c_add():
    bas_ent.insert("end", '+')
def c_sub():
    bas_ent.insert("end", '-')
def c_pow():
    bas_ent.insert("end", '**')
def c_div():
    bas_ent.insert("end", '/')
def c_mod():
    bas_ent.insert("end", '%')
def c_left_brac():
    bas_ent.insert("end", '[')
def c_right_brac():
    bas_ent.insert("end", ']')
#--------------------------------------------------------
def c_clear():
    bas_ent.delete(0, 'end')
    display.delete(1.0,'end')

def valuate():
    display.delete(1.0,'end')
    expression = bas_ent.get()
    if (len(expression) != 0):
        try:
            res = eval(expression)
        except NameError:
            res = "Syntax Error"
    else:
        res = 0
    display.insert(1.0,res)

#=====================================================WIDGETS====================================================

bas_label1 = ttk.Label(frame1, text = "Booooooriiing calcu", font = "bold")
bas_label1.place( x= 400, y = 0)

bas_label2 = ttk.Label(frame1, text = "Chodyam ivde adikk : ", font = "bold")
bas_label2.place(x=40, y =50)

bas_label3 = ttk.Label(frame1, text = "Ithan Utharam : ", font = "bold")
bas_label3.place(x=40, y =150)

enter_exp = tk.StringVar
bas_ent = ttk.Entry(frame1, textvariable = enter_exp, width = 70)          #entry
bas_ent.place(x= 250, y =50)

bas_calc = ttk.Button(frame1, text = "Calculate Expression", command = valuate)
bas_calc.place(x=470, y = 480)
instru = ttk.Label(frame1, text = "Use keyboard or on-screen Keypad to enter expression.")
instru.place(x= 20, y= 600)

display = tk.Text(frame1, width = 40, height = 2)                       #output
display.place(x= 330, y = 150)
#display.configure(state='disabled')
#------------------------------------------------------------------------------------
exp_frame = ttk.LabelFrame(frame1, height = 1000, width = 1100)
exp_frame.place(x = 280, y=250)
one = ttk.Button(exp_frame, text = "1", command = c_one)
one.grid(row =2 , column =0 )
two = ttk.Button(exp_frame, text = "2", command = c_two)
two.grid(row = 2, column =1 )
three = ttk.Button(exp_frame, text = "3", command = c_three)
three.grid(row =2 , column =2 )
four = ttk.Button(exp_frame, text = "4", command = c_four)
four.grid(row =1 , column =0 )
five =ttk.Button(exp_frame, text = "5", command = c_five)
five.grid(row = 1, column =1 )
six = ttk.Button(exp_frame, text = "6", command = c_six)
six.grid(row = 1, column =2 )
seven = ttk.Button(exp_frame, text = "7", command = c_seven)
seven.grid(row =0 , column =0 )
eight = ttk.Button(exp_frame, text = "8", command = c_eight)
eight.grid(row =0 , column =1 )
nine = ttk.Button(exp_frame, text = "9", command = c_nine)
nine.grid(row = 0, column = 2)
zero = ttk.Button(exp_frame, text = "0", command = c_zero)
zero.grid(row =3 , column = 0)
dot = ttk.Button(exp_frame, text = ".", command = c_dot)
dot.grid(row =3 , column =1 )
left_brac = ttk.Button(exp_frame, text = "(", command = c_left_brac)
left_brac.grid(row = 0, column =3 )
right_brac = ttk.Button(exp_frame, text = ")", command = c_right_brac)
right_brac.grid(row = 0, column =4 )
bas_add = ttk.Button(exp_frame, text = "+", command = c_add)
bas_add.grid(row =2 , column = 3)
bas_subs = ttk.Button(exp_frame, text = "-", command = c_sub)
bas_subs.grid(row = 2, column =4 )
bas_multi = ttk.Button(exp_frame, text = "X", command = c_prod)
bas_multi.grid(row = 1, column =3 )
bas_div = ttk.Button(exp_frame, text = "/", command = c_div)
bas_div.grid(row =1 , column = 4)
bas_reminder =ttk.Button(exp_frame, text = "Reminder", command = c_mod)
bas_reminder.grid(row =3 , column =2 )
expo = ttk.Button(exp_frame, text = "Power", command = c_pow)
expo.grid(row = 3, column =3 )
clear = ttk.Button(exp_frame, text = "Clear", command = c_clear)
clear.grid(row = 3, column =4 )

#======================================================END================================================
frame1.mainloop()