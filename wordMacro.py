from tkinter import messagebox
import tkinter as tk
import pyautogui
import time
import sys

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

def button_event_1():
    if var1.get() == '':
        tk.messagebox.showerror('message', 'nothing is typed, type again')
    else:
        tk.messagebox.showinfo('message', 'done')

def button_event_2():
    if var2.get() == '':
        tk.messagebox.showerror('message', 'nothing is typed, type again')
    elif type(var2.get) != str:
        tk.messagebox.showerror('message', 'wrong type of input, type again')
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
    print("Process Success")

def button_event_4():
    sys.exit()

window = tk.Tk()
window.title('N')
window.geometry('400x350')
window.configure(background='white')
div_size = 25
div_height = 5
div_1 = tk.Label(window, text="WordMacro", font=('Arial', 12), height=5, background='white')
div_1.grid(column=0,row=0,columnspan=2)
div_2 = tk.Label(window, text="Wassup", font=('Arial', 12), width=div_size, height=div_height, background='white')
div_2.grid(column=0,row=1,sticky="W",rowspan=2)
var1 = tk.StringVar()
msg = tk.Entry(window, textvariable=var1)
msg.grid(column=1,row=1,ipadx=5,sticky="E")
button1 = tk.Button(window, text='Enter', command=button_event_1)
button1.grid(row=2, column=1)
div_3 = tk.Label(window, text="how many times you want?", font=('Arial', 12), width=div_size, height=div_height, background='white')
div_3.grid(column=0,row=3,sticky="W",rowspan=2)
var2 = tk.IntVar()
times = tk.Entry(window, textvariable=var2)
times.grid(column=1,row=3,ipadx=5,sticky="E")
button2 = tk.Button(window, text='Enter', command=button_event_2)
button2.grid(row=4, column=1)
button3 = tk.Button(window, text='GO!!', command=button_event_3)
button3.grid(row=5, column=0,pady=15)
button4 = tk.Button(window, text='Quit', command=button_event_4)
button4.grid(row=5, column=1,pady=15)
window.mainloop()