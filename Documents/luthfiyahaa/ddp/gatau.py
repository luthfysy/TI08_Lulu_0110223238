from tkinter import *

def klik_tombol(angka):
    current = str(input_field.get())
    new = current + str(angka)
    input_field.delete(0, END)
    input_field.insert(0, new)

root = Tk()
root.title("Aplikasi Kalkulator")

input_field = Entry(root)
input_field.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    Button(root, text=button, padx=20, pady=20, command=lambda button=button: klik_tombol(button)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()

def hitung():
    try:
        expression = input_field.get()
        result = eval(expression)
        input_field.delete(0, END)
        input_field.insert(0, result)
    except:
        input_field.delete(0, END)
        input_field.insert(0, "Error")