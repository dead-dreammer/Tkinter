import tkinter as tk

# create the window
cal = tk.Tk()

# set size that the window should open to
cal.geometry('400x300')

# give the window a title
cal.title('Question 2.2')

# create the lables 
label_1 = tk.Label(cal, text = "Enter the score for test 1 :")
label_2 = tk.Label(cal, text = "Enter the score for test 2 :")
label_3 = tk.Label(cal, text = "Enter the score for test 3 :")
label_ave = tk.Label(cal, text = "Average :")
label_blk = tk.Label(cal, text = " ")

# create entries for the user to input values
entry_1 = tk.Entry(cal)
entry_2 = tk.Entry(cal)
entry_3 = tk.Entry(cal)

# create the function that calculates and displays the average of the numbers
def average():

    # get the values from the enteries
    test1 = float(entry_1.get())
    test2 = float(entry_2.get())
    test3 = float(entry_3.get())

    # calculate the average
    Average = (test1 + test2 + test3)/3

    # display the average
    label_blk.configure(text = f"{Average:.2f}")

# create the function that is called when the quit button is pressed
def close():
    cal.quit()

# create buttons 
button_1 = tk.Button(cal, text = "Average", command = average)
button_2 = tk.Button(cal, text = "Quit", command = close)

# Placing widgets on window using grid format
label_1.grid(row = 0, column = 0, columnspan = 3, ipadx = 10, ipady = 10, padx = 35, pady = 10)
label_2.grid(row = 1, column = 0, columnspan = 3, ipadx = 10, ipady = 10, padx = 35)
label_3.grid(row = 2, column = 0, columnspan = 3, ipadx = 10, ipady = 10, padx = 35, pady = 10)
label_ave.grid(row = 3, column = 1,columnspan = 2, padx = 20, pady = 20)
label_blk.grid(row = 3, column = 3, columnspan = 2)

entry_1.grid(row = 0, column = 3)
entry_2.grid(row = 1, column = 3)
entry_3.grid(row = 2, column = 3)

button_1.grid(row = 4, column = 1, columnspan = 2, ipadx = 25, ipady = 10, padx = 35, pady = 10)
button_2.grid(row = 4, column = 3,columnspan = 2, ipadx = 25, ipady = 10)

# close the window
cal.mainloop()