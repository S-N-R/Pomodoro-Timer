import time
import os
import ctypes
from tkinter import *
from tkinter import messagebox

window = Tk()
var = StringVar()

def click():
    messagebox.showinfo(title='Timer Starting', message='Get ready, the timer is starting.')
    workmins = 5

    for x in range(workmins, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        var.set(f"00:{minutes:02}:{seconds:02}")
        print(f"00:{minutes:02}:{seconds:02}")
        window.update()
        time.sleep(1)

    root = Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    messagebox.showwarning(title='BREAK TIME',message='TAKE A FIVE MINUTE BREAK', parent=root)
    root.destroy()
    print('TAKE A FIVE MINUTE BREAK')


window.title("Pomodoro Timer")
window.configure(background="darkgrey")
window.minsize(275, 150)
window.maxsize(275, 150)
window.geometry("275x150")

lb = Label(window, textvariable=var, font='Ariel')
lb.pack(pady=10)

button = Button(window, command=click,text='Start Pomodoro Timer')
button.pack()

window.mainloop()

