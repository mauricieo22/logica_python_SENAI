import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

def enter_pressionado(event):
    label.config(text=widget.event.widget.get())

label = tk.Label(root, text="Digite seu texto aqui:")
label.pack()

entry = tk.Entry(root)
entry.insert(0, " ")
entry.bind("<Return>", enter_pressionado)
entry.bind("<Tab>", enter_pressionado)
entry.pack()

label.pack()

root.mainloop()