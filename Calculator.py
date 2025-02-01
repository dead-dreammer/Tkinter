#Calculator
import tkinter as tk
cal = tk.Tk()

entry = tk.Entry(cal,text=" ")
entry.grid(  row=0, column=0, columnspan=2, ipadx = 40, ipady = 10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_no = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_no)
    entry.delete(0, tk.END)

def button_sub():
    first_no = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_no)
    entry.delete(0, tk.END)


def button_multiply():
    first_no = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_no)
    entry.delete(0, tk.END)


def button_div():
    first_no = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_no)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    
    if (math == "addition"):
        entry.insert(0, f_num + int(second_number))

    elif (math == "subtraction"):
        entry.insert(0, f_num - int(second_number))

    elif (math == "multiplication"):
        entry.insert(0, f_num * int(second_number))

    elif (math == "division"):
        entry.insert(0, f_num / int(second_number))



    
button_1 = tk.Button(cal, text="1",pady=20, padx=40, command = lambda: button_click(1))
button_2 = tk.Button(cal, text="2",pady=20, padx=40, command = lambda: button_click(2))
button_3 = tk.Button(cal, text="3",pady=20, padx=40, command = lambda: button_click(3))
button_4 = tk.Button(cal, text="4",pady=20, padx=40, command = lambda: button_click(4))
button_5 = tk.Button(cal, text="5",pady=20, padx=40, command = lambda: button_click(5))
button_6 = tk.Button(cal, text="6",pady=20, padx=40, command = lambda: button_click(6))
button_7 = tk.Button(cal, text="7",pady=20, padx=40, command = lambda: button_click(7))
button_8 = tk.Button(cal, text="8",pady=20, padx=40, command = lambda: button_click(8))
button_9 = tk.Button(cal, text="9",pady=20, padx=40, command = lambda: button_click(9))
button_0 = tk.Button(cal, text="0",pady=20, padx=40, command = lambda: button_click(0))
button_add = tk.Button(cal, text="+",pady=20, padx=40, command = button_add, bg="orange", fg="white")
button_equal = tk.Button(cal, text="=",pady=20, padx=45, command = button_equal, bg="green", fg="white")
button_clear= tk.Button(cal, text="clear",pady=20, padx=30, command = button_clear, bg="red", fg="white")

button_sub = tk.Button(cal, text="-",pady=20, padx=40, command = button_sub, bg="orange", fg="white" )
button_multiply = tk.Button(cal, text="*",pady=20, padx=40, command = button_multiply , bg="orange", fg="white")
button_div = tk.Button(cal, text="/",pady=20, padx=40, command = button_div  ,bg="orange", fg="white")

button_1.grid (padx=5, pady=5, row=1, column=0)
button_2.grid( padx=5, pady=5, row=1, column=1)
button_3.grid( padx=5, pady=5,row=1, column=2)
button_4.grid( padx=5, pady=5,row=2, column=0)
button_5.grid( padx=5, pady=5,row=2, column=1)
button_6.grid( padx=5, pady=5,row=2, column=2)
button_7.grid( padx=5, pady=5,row=3, column=0)
button_8.grid( padx=5, pady=5,row=3, column=1)
button_9.grid( padx=5, pady=5,row=3, column=2)
button_0.grid( padx=5, pady=5,row=4, column=0)
button_add.grid( row=4, column=1)
button_sub.grid( row=4, column=2)

button_equal.grid( row=6, column=2)
button_clear.grid( row=0, column=2)


button_multiply.grid( row=6, column=0)
button_div.grid( row=6, column=1)

cal.mainloop()