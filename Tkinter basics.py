import tkinter as tk

#create parent container TK() for other widgets
#it is the main window for the foundation GUI

root = tk.Tk() 

# set title of window
root.title("My Tkinter window")

#set size of window (width x height)
root.geometry("400x300")

#set background color
root.configure(bg = "purple")

#call the main event loop to keep the window running and responsive
#to user interactions until window is xlosed
#root.mainloop()

label = tk.Label(root, text= "HELLO ALEX!")

#set width of entry
entry = tk.Entry(root, width = 20, borderwidth = 5)
entry.insert(0,"enter your age")

def click_2():
    label_4= tk.Label(root, text=entry.get())
    label_4.pack()
button =  tk.Button(root, text = "submit", command=click_2, bg= "blue", fg = "white")
#function must come before button if its being called

#get function gets your value

label_2= tk.Label(root, text="bye alex")
#state determines state of button and disables it 
#pad determines the size of the button

def click():
    label_3 = tk.Label(root, text="You clicked me, yay")
    label_3.pack()
    button_2.configure(bg="blue", fg="white")

button_2 = tk.Button(root, text = "click me", command=click, fg="white", bg="red")
#command calls the function

# pack shoves it onto screen
#pack keeps it exactly where its supposed to be- absolute
label.pack()
entry.pack()
button.pack()
button_2.pack()
label_2.pack()
root.mainloop()

