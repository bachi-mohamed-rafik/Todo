import sqlite3
import tkinter as tk
from tkinter import *
import sqlite3
import pandas as pd
from tabulate import tabulate
import sys

root=Tk()
root.title('TODO LIST')
root.iconbitmap('C:/Users/Bachi/Desktop/GUI/clock_icon.ico')
root.geometry("400x800")
root.configure(background = "gray")
root.resizable(False,False)
# initialize list  
test_list = [] 




counter = 1  


# initialize string  
test_str = 'kkkkkk'
  






#Connect to database
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()


#Commit our command
conn.commit()

#Close our connection
conn.close()

# global list is declare for storing all the task 
tasks_list = [] 



# global variable is declare for couting the task 
counter = len(tasks_list)

global ENTRY_BOX    
global ENTRY_ID



def add():
    global counter 
    test_list.append(ENTRY_BOX.get())
    T.insert(INSERT,  ENTRY_BOX.get()) 

    # incremented 
    counter += 1
    ENTRY_BOX.delete(0, END)
    show()





def delet():
    test_list.pop(int(ENTRY_ID.get()))
    ENTRY_ID.delete(0, END)
    show()


def close_window(): 
    root.destroy()


########################################################################################################################################################




ENTRY_label = Label(root , text="Enter Your Task" ,bg="rosybrown")
ENTRY_label.pack(padx=3, pady=5 , ipadx=3, ipady=5)



ENTRY_BOX = tk.Entry(root, width=20)
ENTRY_BOX.pack(padx=3, pady=5 , ipadx=3, ipady=5)



Save_Button = Button(root , text="Submit", bg="slategrey" , command = add)
Save_Button.pack(padx=3, pady=5 , ipadx=3, ipady=5)



T = tk.Text(root, width=40)
T.pack()


Show_tasks = Label(root, text="Delete Task Number" ,bg="rosybrown")
Show_tasks.pack(padx=3, pady=5 , ipadx=3, ipady=5)



ENTRY_ID = Entry(root, width=5)
ENTRY_ID.pack(padx=3, pady=5 , ipadx=3, ipady=5)

rid = ENTRY_ID.get()

Delete_Button = Button(root , text="Delete", bg="slategrey" , command= delet)
Delete_Button.pack(padx=3, pady=5 , ipadx=3, ipady=5)



back_Button = Button(root , text="Exit", bg="slategrey" , command=close_window)
back_Button.pack(padx=3, pady=5 , ipadx=3, ipady=5)



def show():
    T.delete('1.0', END)
    for num, name in enumerate(test_list, start=1):
        msg="test_list {}: {}".format(num-1, name)
        T.insert(tk.END, msg)
        T.insert(tk.END, '\n')






root.mainloop()
