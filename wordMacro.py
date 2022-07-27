from importlib.resources import path
from tkinter import messagebox
import tkinter as tk
import pyautogui
import time
import sys

class gui:
    def __init__(self):

        def validate(P):
            print(P)
            if str.isdigit(P) or P == '':
                return True
            else:
                return False

        self.window = tk.Tk()
        self.window.title('Word Macro')
        self.window.geometry('600x700')
        self.window.configure(background='azure3')
        self.div_size = 35
        self.div_height = 7
        self.div_1 = tk.Label(self.window, text="WordMacro", font=('Arial', 12), height=5, background='azure3')
        self.div_1.grid(column=0,row=0,columnspan=2)
        self.div_2 = tk.Label(self.window, text="Discord Path", font=('Arial', 12), width=self.div_size, height=self.div_height, background='azure3')
        self.div_2.grid(column=0,row=1,sticky="W",rowspan=2)
        self.var1 = tk.StringVar()
        self.path = tk.Entry(self.window, textvariable=self.var1)
        self.path.grid(column=1,row=1,padx=5,sticky="E")
        self.button1 = tk.Button(self.window, text='Enter', command=self.button_event_1, font=('Arial', 12))
        self.button1.grid(row=2, column=1)
        self.div_3 = tk.Label(self.window, text="Wassup", font=('Arial', 12), width=self.div_size, height=self.div_height, background='azure3')
        self.div_3.grid(column=0,row=3,sticky="W",rowspan=2)
        self.var2 = tk.StringVar()
        self.msg = tk.Entry(self.window, textvariable=self.var2)
        self.msg.grid(column=1,row=3,padx=5,sticky="E")
        self.button2 = tk.Button(self.window, text='Enter', command=self.button_event_2, font=('Arial', 12))
        self.button2.grid(row=4, column=1)
        self.div_4 = tk.Label(self.window, text="how many times you want?", font=('Arial', 12), width=self.div_size, height=self.div_height, background='azure3')
        self.div_4.grid(column=0,row=5,sticky="W",rowspan=2)
        vcmd = self.window.register(validate)
        self.var3 = tk.IntVar()
        self.times = tk.Entry(self.window, textvariable=self.var3, validate="key", validatecommand=(vcmd, '%P'))
        self.times.grid(column=1,row=5,padx=5,sticky="E")
        self.button3 = tk.Button(self.window, text='Enter', command=self.button_event_3, font=('Arial', 12))
        self.button3.grid(row=6, column=1)
        self.button4 = tk.Button(self.window, text='GO!!', command=self.button_event_4, font=('Arial', 12))
        self.button4.grid(row=7, column=0,pady=35)
        self.button5 = tk.Button(self.window, text='Quit', command=self.button_event_5, font=('Arial', 12))
        self.button5.grid(row=7, column=1,pady=35)
        self.window.mainloop()

    def spam(self):
        msg1 = self.var2.get()
        pyautogui.typewrite(msg1)
        time.sleep(0.2)
        pyautogui.press("enter")
        time.sleep(0.2)

    def button_event_1(self):
        if self.var1.get() == '':
            tk.messagebox.showerror('message', 'nothing is typed, type again')
        else:
            tk.messagebox.showinfo('message', 'done')

    def button_event_2(self):
        if self.var2.get() == '':
            tk.messagebox.showerror('message', 'nothing is typed, type again')
        else:
            tk.messagebox.showinfo('message', 'done')

    def button_event_3(self):
        if self.var3.get() == '':
            tk.messagebox.showerror('message', 'nothing is typed, type again')
        else:
            tk.messagebox.showinfo('message', 'done')

    def button_event_4(self):
        path1 = self.var1.get()
        print("Opening discord...")
        time.sleep(1)
        pyautogui.hotkey('win','r')
        time.sleep(1)
        pyautogui.typewrite(path1)
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.click(499,989)
        time.sleep(1)
        print("Process Success")
        time.sleep(1)
        print("Spaming the message...")
        realTime = 0
        times = self.var3.get()
        while realTime < times:
            self.spam()
            realTime += 1
            realTimeStr = str(realTime)
            print("times: " + realTimeStr)
        print("Process Success")

    def button_event_5(self):
        sys.exit()

gui()