import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

def valor_mudou(evento):
    label.config(text=evento)

scale = tk.Scale(root, from_ = 0, to = 100, orient = "horizontal", command= valor_mudou)
scale.pack()

label = tk.Label(root, text="0")
label.pack()

root.mainloop()