import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("CHECKBOX")
root.geometry("300x100")

checkbox_estado = tk.IntVar()

def mostrar_estado():
    if checkbox_estado.get():
        txt = "Checked"

    else:
        txt = "Unchecked"
    checkbox.config(text=f"Check me!({txt})")

checkbox = tk.Checkbutton(root, text= "Check me! (Checked)", variable=checkbox_estado, command=mostrar_estado)
checkbox.deselect()
checkbox.pack(expand=False)

root.mainloop()