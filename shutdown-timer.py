import time
import os
from tkinter import *

def starttimer():
    minutes = insert_time_entry.get()
    minutes = int(minutes)
    minutes = minutes * 60
    
    countdown(minutes)

def shutdown():
     os.system('shutdown -s -t 0')

def countdown(n):
     while n:
          time.sleep(1)
          n = n - 1
     shutdown()

main = Tk()
main.title('Shutdown timer')
main.geometry('350x400')

heading = Label(main, text='Shutdown-Timer', font=('sans-serif', 18))
heading.pack()

insert_time_entry = Entry(main)
insert_time_entry.pack()

enter_time_button = Button(main, text='Enter', command=starttimer)
enter_time_button.pack()


main.mainloop()
