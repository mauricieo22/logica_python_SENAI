import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Desinvolvimento de Sistemas")
root.geometry("400x250")


label_moeda = tk.Label(root, text="Valor: ")
tk.Label(root, text="Valor: ").grid(row=0,column=0,padx=5,pady=5,sticky="we")

entry_moeda = tk.Entry(root)
entry_moeda.grid(row=0,column=1,padx=5,pady=5,sticky="we")

label_origem = tk.Label(root, text="Moeda de Origem: ") 
label_origem.grid(row=1,column=1,padx=5,pady=5,sticky="we")

combobox = ttk.Combobox(root, values = ["USD", "BRL", "EUR"])
combobox.grid(row=1,column=2,padx=5,pady=5,sticky="we")

label_destino = tk.Label(root, text="Moeda de Destino: ") 
label_destino.grid(row=2,column=1,padx=5,pady=5,sticky="we")

combobox = ttk.Combobox(root, values = ["USD", "BRL", "EUR"])
combobox.grid(row=2,column=2,padx=5,pady=5,sticky="we")


root.mainloop()