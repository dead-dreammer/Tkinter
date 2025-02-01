import tkinter as tk

# create a window
display = tk.Tk()

# set the size that the window should open to
display.geometry('400x300')

# give the window a title
display.title('Question 2.1')

# create the function that displays text
def show():
    
    # create labels that show text
    label_1 = tk.Label(display, text = "Dalziel Alexander Sarkhot")
    label_2 = tk.Label(display, text = "169 Bridgevale Crescent")
    label_3 = tk.Label(display, text = "Durban, Rydalvale 4068")

    # place the labels on the window using grid
    label_1.place(x= 140, y = 40)
    label_2.place(x= 140, y = 60)
    label_3.place(x= 140, y = 80)

# create the function that is called when the quit button is pressed
def close():
    display.quit()

# create the buttons
button_1 = tk.Button(display, text = "Show info", command = show, padx = 15, pady = 10)
button_2 = tk.Button(display, text = "Quit", command = close, padx = 15, pady = 10)

# Placing widgets on the window using grid
button_1.place(x = 120, y = 150)
button_2.place(x = 220, y = 150)

# close the window
display.mainloop()