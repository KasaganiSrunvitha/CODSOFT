from tkinter import *
from tkinter import messagebox as mb

# Initialize the main window
t = Tk()
t.title("Calculator")
t.geometry("312x324")

# Create a frame for the calculator buttons
frame = Frame(master=t, bg="skyblue", padx=10)
frame.pack()

# Entry widget for the calculator display
entry = Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, padx=2)

# Define button click function
def click(n):
    entry.insert(END, n)

# Define clear function
def clear():
    entry.delete(0, END)

# Define equal function
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, END)
        entry.insert(0, y)
    except:
        mb.showinfo("Error", "Syntax Error")

# Create calculator buttons
b1 = Button(master=frame, text='1', padx=15, pady=5, width=3, command=lambda: click(1))
b1.grid(row=1, column=0, pady=2)

b2 = Button(master=frame, text='2', padx=15, pady=5, width=3, command=lambda: click(2))
b2.grid(row=1, column=1, pady=2)

b3 = Button(master=frame, text='3', padx=15, pady=5, width=3, command=lambda: click(3))
b3.grid(row=1, column=2, pady=2)

b4 = Button(master=frame, text='4', padx=15, pady=5, width=3, command=lambda: click(4))
b4.grid(row=2, column=0, pady=2)

b5 = Button(master=frame, text='5', padx=15, pady=5, width=3, command=lambda: click(5))
b5.grid(row=2, column=1, pady=2)

b6 = Button(master=frame, text='6', padx=15, pady=5, width=3, command=lambda: click(6))
b6.grid(row=2, column=2, pady=2)

b7 = Button(master=frame, text='7', padx=15, pady=5, width=3, command=lambda: click(7))
b7.grid(row=3, column=0, pady=2)

b8 = Button(master=frame, text='8', padx=15, pady=5, width=3, command=lambda: click(8))
b8.grid(row=3, column=1, pady=2)

b9 = Button(master=frame, text='9', padx=15, pady=5, width=3, command=lambda: click(9))
b9.grid(row=3, column=2, pady=2)

b10 = Button(master=frame, text='+', padx=15, pady=5, width=3, command=lambda: click('+'))
b10.grid(row=4, column=0, pady=2)

b11 = Button(master=frame, text='-', padx=15, pady=5, width=3, command=lambda: click('-'))
b11.grid(row=4, column=1, pady=2)

b12 = Button(master=frame, text='', padx=15, pady=5, width=3, command=lambda: click(''))
b12.grid(row=4, column=2, pady=2)

b13 = Button(master=frame, text='/', padx=15, pady=5, width=3, command=lambda: click('/'))
b13.grid(row=5, column=0, pady=2)

b14 = Button(master=frame, text='%', padx=15, pady=5, width=3, command=lambda: click('%'))
b14.grid(row=5, column=1, pady=2)

b15 = Button(master=frame, text='=', padx=15, pady=5, width=3, command=equal)
b15.grid(row=5, column=2, pady=2)

b16 = Button(master=frame, text='clear', padx=15, pady=5, width=8, command=clear)
b16.grid(row=6, column=0, columnspan=2, pady=2)

b17 = Button(master=frame, text='0', padx=15, pady=5, width=3, command=lambda: click(0))
b17.grid(row=6, column=2, pady=2)

# Run the main event loop
t.mainloop()
