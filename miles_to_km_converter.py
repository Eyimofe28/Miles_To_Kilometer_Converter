from tkinter import *
from tkinter import messagebox


def calculate():
    if miles.get().isdigit():
        km = float(miles.get()) * 1.609
        kilometer.config(text=str(round(km, 2)))
    else:
        messagebox.showerror(title="ERROR", message="Invalid Input. Please enter numbers only.\n(Spaces not allowed).")


window = Tk()
window.minsize(width=220, height=130)
window.resizable(width=False, height=False)
window.title("Miles to Km Converter")
window.config(background='black', pady=20, padx=15)

space = Label(window, bg="black")
space.grid(row=0, column=0)

miles = Entry(window, font=("Arial", 12, "bold"), fg="black", bg="white", width=9)
miles.insert(END, string="0")
miles.grid(row=0, column=1)

milesLabel = Label(window, font=("Times New Roman", 12), fg="white", bg="black", text="Miles")
milesLabel.grid(row=0, column=2)
milesLabel.config(padx=10)

text = Label(window, font=("Times New Roman", 12), fg="white", bg="black", text="is equal to")
text.grid(row=1, column=0)
text.config(pady=15)

kilometer = Label(window, font=("Times New Roman", 12), fg="light blue", bg="black", text="0.0")
kilometer.grid(row=1, column=1)
kilometer.config(pady=15)

kilometerLabel = Label(window, font=("Times New Roman", 12), fg="white", bg="black", text="KM")
kilometerLabel.grid(row=1, column=2)
kilometerLabel.config(pady=15)

button = Button(window, font=("Times New Roman", 10), fg="black", bg="white", text="Calculate", command=calculate)
button.grid(row=2, column=1)
button.config()

window.mainloop()
