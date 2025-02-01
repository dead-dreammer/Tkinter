import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkmb

def button_functions():
    submit()
    display()

def submit():
    name = entry_name.get()
    surname = entry_surname.get()
    label_result.configure(text = f"{name} {surname}")
    tkmb.showinfo('Response', 'Thanks for clicking the button!')

def comboFunction(event):
    gender= combo_gender.get()
    print(gender)

def display():
    name = entry_name.get()
    surname = entry_surname.get()
    radio = radio_variable.get()
    hours = spibox_hours.get()
    gender= combo_gender.get()
    
    selected_item = selected_item = listbox.get(tk.ACTIVE)

    label_1 = tk.Label(window, text = "")
    label_2 = tk.Label(window, text = "")
    label_3 = tk.Label(window, text = "")
    label_1.configure(text = f"{name} {surname}")
    label_2.configure(text = f"{hours} hours {selected_item}")
    label_3.configure(text = f"{radio} {gender}")
    label_1.grid(row=6, column=1)
    label_2.grid(row=7, column=1)
    label_3.grid(row=8, column=1)


window = tk.Tk ()
window.title("User information form")

label_name = tk.Label(window, text="Name:")
label_surname = tk.Label(window, text="Surname:")
label_days = tk.Label(window, text="Days:")
label_hours = tk.Label(window,text="hours:")
label_gender=tk.Label(window, text="Gender:")
label_result = tk.Label(window, text="")

entry_name = tk.Entry(window)
entry_surname=tk.Entry(window)

spibox_hours= tk.Spinbox(window , from_= 0,to = 24,increment = 1,width = 5)

radio_variable = tk.StringVar()
radio_button1=tk.Radiobutton(window, text="Male",variable=radio_variable,value="Male")
radio_button2=tk.Radiobutton(window, text="Female",variable=radio_variable,value="Female")
radio_button3=tk.Radiobutton(window, text="other",variable=radio_variable,value="other")


listbox=tk.Listbox(window,selectmode= tk.SINGLE)
days =  ["Oct 15", "Oct 16", "Oct 17", "Oct 18", "Oct 19", "Oct 20", "Oct 21", "Oct 22", "Oct 23","Oct 24", "Oct 25", "Oct 26", "Oct 27", "Oct 28", "Oct 29", "Oct 30", "Oct 31"]
for day in days:
    listbox.insert(tk.END,day)

submit_button = tk.Button(window,text ="Submit",command=button_functions)

#how to do a "combo box " or a drop down.
gender = ["Male","Female","other"]
combo_gender = ttk.Combobox(window, values= gender)
combo_gender.set("Male")
combo_gender.bind('<<ComboboxSelected>>', comboFunction)


label_name.grid(row=0, column=0, padx=10 , pady=10)
entry_name.grid(row=0,column=1, padx=10 , pady=10)

label_surname.grid(row=1, column=0, padx=10, pady=10)
entry_surname.grid(row=1,column=1, padx=10 , pady=10)

label_days.grid(row=3,column=0, padx=10 , pady=10)
listbox.grid(row=3,column=1, padx=10 , pady=10)

label_hours.grid(row=4, column=0, padx=10, pady=10)
spibox_hours.grid(row=4, column=1, padx=10, pady=10)

label_gender.grid(row=5, column=0, padx=10, pady=10)
radio_button1.grid(row=6, column=0, padx=10, pady=10)
radio_button2.grid(row=7, column=0, padx=10, pady=10)
radio_button3.grid(row=8, column=0, padx=10, pady=10)
combo_gender.grid(row=5, column=1, padx=10, pady=10)

label_result.grid(row=9, column=0, padx=10, pady=10)

submit_button.grid(row=10, column=0,columnspan = 2,  padx=10, pady=10)

window.mainloop()