import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

def button_command():
    messagebox.showinfo(
        "Informação",
        "Você clicou no botão 1!"
    )

button = tk.Button(root,text="Clique aqui 1",command=button_command)

def button_command2():
    messagebox.showerror(
        "Aviso",
        "Você clicou no botão 2!"
    )

button2 = tk.Button(root,text="Clique aqui 2",command=button_command2)

button.pack()
button2.pack()

root.mainloop()