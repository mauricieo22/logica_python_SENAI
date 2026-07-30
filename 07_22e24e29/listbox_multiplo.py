import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("CHECKBOX")
root.geometry("600x300")

def selecao_mudou(evento):
    sel = evento.widget.curselection()
    if sel:
        itens = [evento.widget.get(i) for i in sel]
        label.config(text=f"{",".join(itens)} selecionado(s)!")

listbox = tk.Listbox(root, selectmode="multiple")
for item in ["Primeiro", "Segundo", "Terceiro"]:
    listbox.insert(tk.END, item)

listbox.bind("<<ListboxSelect>>", selecao_mudou)
listbox.pack(expand=True)

label= tk.Label(root, text="Primeiro selecionado!")
label.pack()

root.mainloop()