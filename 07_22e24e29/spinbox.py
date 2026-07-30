#StringVar é uma variável que armazena uma string
#É usada para atualizar o widget dinamicamente

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

spinbox_var = tk.StringVar(value="0")

spinbox = tk.Spinbox(root, from_= -10, to= 10,
                     #increment = 5,
                     textvariable=spinbox_var)

spinbox.pack(expand=True)

label = tk.Label(root, textvariable=spinbox_var)
label.pack()

root.mainloop()