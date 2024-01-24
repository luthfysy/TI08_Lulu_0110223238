import tkinter as tk
from tkinter import ttk
import math

#root
root = tk.Tk()
root.geometry('700x350')
root.title = ('Menghitung jarak antar kota')

jarak = 0
bogor = 120.6
jakarta = 25
bekasi = 35.7
depok = 5   

def jarak_kota(kota):
    if kota == 'bogor':
        jarak += bogor
    elif kota == 'jakarta':
        jarak += jakarta
    elif kota == 'bekasi':
        jarak += bekasi
    elif kota == 'depok':
        jarak += depok
    
#wiget
margin = ttk.Frame(master=root)
margin.pack()

title = ttk.Label(master=root,text='Menghitung Jarak Antar Kota', font='Arial 16 bold')
title.pack()

input_frame = ttk.Frame(master=root)
input_frame.pack()

label = ttk.Label(master=root, text='Kota Tujuan : ', font='arial 12')
label.pack(pady=5)

entry_var = tk.StringVar()
entry_var = ttk.Entry(master=root, width=20, textvariable=entry_var)
entry_var.pack(pady=5)

button = ttk.Button(master=root, text='Hitung',command='calculate')
button.pack(pady=5)

Kota_Label = tk.Label(master=root, text='JARAK KOTA : ', font='arial 14 bold')
Kota_Label.pack()

#run
root.mainloop()