from tkinter import messagebox
import tkinter as tk
import pyautogui
import time
import sys

class gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Word Macro')
        self.window.geometry('400x350')
        self.window.configure(background='white')
        self.div_size = 25
        self.div_height = 5
        self.div_1 = tk.Label(self.window, text="WordMacro", font=('Arial', 12), height=5, background='white')
        self.div_1.grid(column=0,row=0,columnspan=2)
        self.div_2 = tk.Label(self.window, text="Wassup", font=('Arial', 12), width=self.div_size, height=self.div_height, background='white')
        self.div_2.grid(column=0,row=1,sticky="W",rowspan=2)
        self.var1 = tk.StringVar()
        self.msg = tk.Entry(self.window, textvariable=self.var1)
        self.msg.grid(column=1,row=1,ipadx=5,sticky="E")
        self.button1 = tk.Button(self.window, text='Enter', command=self.button_event_1)
        self.button1.grid(row=2, column=1)
        self.div_3 = tk.Label(self.window, text="how many times you want?", font=('Arial', 12), width=self.div_size, height=self.div_height, background='white')
        self.div_3.grid(column=0,row=3,sticky="W",rowspan=2)
        self.var2 = tk.IntVar()
        self.times = tk.Entry(self.window, textvariable=self.var2)
        self.times.grid(column=1,row=3,ipadx=5,sticky="E")
        self.button2 = tk.Button(self.window, text='Enter', command=self.button_event_2)
        self.button2.grid(row=4, column=1)
        self.button3 = tk.Button(self.window, text='GO!!', command=self.button_event_3)
        self.button3.grid(row=5, column=0,pady=15)
        self.button4 = tk.Button(self.window, text='Quit', command=self.button_event_4)
        self.button4.grid(row=5, column=1,pady=15)
        self.window.mainloop()
    def click(self):
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

    def spam(self):
        msg1 = self.var1.get()
        print("Spaming the message...")
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
        elif type(self.var2.get) != str:
            tk.messagebox.showerror('message', 'wrong type of input, type again')
        else:
            tk.messagebox.showinfo('message', 'done')

    def button_event_3(self):
        self.click()
        realTime = 0
        times = self.var2.get()
        while realTime < times:
            self.spam()
            realTime += 1
            realTimeStr = str(realTime)
            print("times: " + realTimeStr)
        print("Process Success")

    def button_event_4():
        sys.exit()

gui()