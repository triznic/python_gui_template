from cgitb import text
from tkinter import *

def convert():
    kilogram_value = float(e_kilogram.get())
    grams_value = kilogram_value * 1000
    pounds_value = kilogram_value * 2.20462
    ounces_value = kilogram_value * 35.274

    t_grams.delete("1.0","end")
    t_pounds.delete("1.0","end")
    t_ounces.delete("1.0","end")
    t_grams.insert(END,grams_value)
    t_pounds.insert(END,pounds_value)
    t_ounces.insert(END,ounces_value)

window=Tk()

window.geometry("600x300")

t_kg = Label(window, text='Kg')
t_kg.grid(row=0, column=0)

b_convert = Button(window, text='Convert', command=convert)
b_convert.grid(row=0, column=2)

e1_var = StringVar()
e_kilogram = Entry(window,width=10, textvariable=e1_var)
e_kilogram.grid(row=0, column=1)

t_grams = Text(window,height=1, width=20)
t_grams.grid(row=1, column=0)

t_pounds = Text(window,height=1, width=20)
t_pounds.grid(row=1, column=1)

t_ounces = Text(window,height=1, width=20)
t_ounces.grid(row=1, column=2)

window.mainloop()