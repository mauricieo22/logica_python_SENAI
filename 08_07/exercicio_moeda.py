import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Desinvolvimento de Sistemas")
root.geometry("300x170")

taxas ={
    "USD": 1.0,
    "BRL": 5.50,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 157.00
}

label_moeda = tk.Label(root, text="Valor: ")
tk.Label(root, text="Valor: ",fg="black",bg="skyblue").grid(row=0,column=0,padx=5,pady=5,sticky="e")

entry_moeda = tk.Entry(root)
entry_moeda.grid(row=0,column=1,padx=5,pady=5,sticky="we")

label_origem = tk.Label(root, text="Moeda de Origem: ",fg="black",bg="skyblue")
label_origem.grid(row=1,column=0,padx=5,pady=5,sticky="e")

combobox_origem = ttk.Combobox(root, values = ["USD", "BRL", "EUR","GBP","JPY"])
combobox_origem.grid(row=1,column=1,padx=5,pady=5,sticky="e")

label_destino = tk.Label(root, text="Moeda de Destino: ",fg="black",bg="skyblue") 
label_destino.grid(row=2,column=0,padx=5,pady=5,sticky="e")

combobox_destino = ttk.Combobox(root, values = ["USD", "BRL", "EUR","GBP","JPY"])
combobox_destino.grid(row=2,column=1,padx=5,pady=5,sticky="e")

button = tk.Button(root,text="Converter")
button.grid(row=3,column=1,padx=5,pady=5, sticky="we", columnspan=2)

tk.Label(root, text="Resultado: ").grid(row=4,column=0,padx=5,pady=5,sticky="e")
label_resultado = tk.Label(root, text="")
label_resultado.grid(row=4,column=1,padx=5,pady=5,sticky="e")

def converter():
    valor = float(entry_moeda.get())
    origem = combobox_origem.get()
    destino = combobox_destino.get()

    if origem in taxas and destino in taxas:
        resultado = valor * (taxas[destino] / taxas[origem])
        label_resultado.config(text=f"{resultado:.2f} {destino}")
    else:
        label_resultado.config(text="Moeda inválida!")

button.config(command=converter)


root.mainloop()