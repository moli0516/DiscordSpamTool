from tkinter import messagebox
import tkinter as tk
from turtle import left
import pyautogui
import time

def click():
    print("clicking to discord...")
    time.sleep(1)
    pyautogui.click(81,1052)
    time.sleep(0.5)
    pyautogui.click(200,344)
    time.sleep(0.5)
    pyautogui.typewrite("discord")
    time.sleep(0.5)
    pyautogui.click(506,648)
    time.sleep(3)
    pyautogui.click(499,989)
    time.sleep(1)
    print("Process Success")

def spam():
    msg1 = var1.get()
    print("Spaming the message...")
    pyautogui.typewrite(msg1)
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(0.2)
    print("Process Success")

def button_event_1():
    if var1.get() == '':
        tk.messagebox.showerror('message', 'nothing is typed, type again')
    else:
        tk.messagebox.showinfo('message', 'done')

def button_event_2():
    if var2.get() == '':
        tk.messagebox.showerror('message', 'nothing is typed, type again')
    else:
        tk.messagebox.showinfo('message', 'done')

def button_event_3():
    click()
    realTime = 0
    times = var2.get()
    while realTime < times:
        spam()
        realTime += 1
        realTimeStr = str(realTime)
        print("times: " + realTimeStr)

window = tk.Tk()
window.title('N')
window.geometry('800x600')
window.configure(background='white')
div_size = 25
div_height = 10
div_1 = tk.Label(window, text="WordMacro", font=('Arial', 12), width=100, height=4)
div_1.grid(column=0,row=0)
div_2 = tk.Label(window, text="Wassup", font=('Arial', 12), width=div_size, height=div_height)
div_2.grid(column=0,row=1,sticky="W")
var1 = tk.StringVar()
msg = tk.Entry(window, textvariable=var1)
msg.grid(column=1,row=1,sticky="W")
button1 = tk.Button(window, text='done', command=button_event_1)
button1.grid(row=2, column=1)
div_3 = tk.Label(window, text="how many times you want?", font=('Arial', 12), width=div_size, height=div_height)
div_3.grid(column=0,row=3,sticky="W")
var2 = tk.IntVar()
times = tk.Entry(window, textvariable=var2)
times.grid(column=1,row=4,sticky="W")
button2 = tk.Button(window, text='done', command=button_event_2)
button2.grid(row=4, column=1)
button3 = tk.Button(window, text='done', command=button_event_3)
button3.grid(row=5, column=0)
window.mainloop()