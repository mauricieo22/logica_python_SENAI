import tkinter as tk
from tkinter import ttk, messagebox


root = tk.Tk()
root.title("Senai - Desinvolvimento de Sistemas")
root.resizable(False, False)                    

imagem_login = tk.PhotoImage(file="images.png").subsample(3,3)
tk.Label(root, image=imagem_login).grid(row=0, column=0, padx=5, pady=5, sticky="nsw", rowspan=8)

label_nome = tk.Label(root, text="Nome: ")
tk.Label(root, text="Nome: ").grid(row=2,column=1,padx=5,pady=5,sticky="ee")

entry_nome = tk.Entry(root)
entry_nome.grid(row=2,column=2,padx=5,pady=5,sticky="we")

label_genero = tk.Label(root, text="Genero: ") 
label_genero.grid(row=3,column=1,padx=5,pady=5,sticky="ee")
combobox = ttk.Combobox(root, values = ["Masculino", "Feminino", "Outro"])
combobox.grid(row=3,column=2,padx=5,pady=5,sticky="we")

label_cor_olhos = tk.Label(root, text="Cor dos olhos: ") 
label_cor_olhos.grid(row=4,column=1,padx=5,pady=5,sticky="ee")
combobox = ttk.Combobox(root, values = ["Castanho", "Preto", "Azul", "Verde", "Outro"])
combobox.grid(row=4,column=2,padx=5,pady=5,sticky="we")

label_altura = tk.Label(root, text="Altura(cm): ") 
label_altura.grid(row=5,column=1,padx=5,pady=5,sticky="ee")
entry_altura = tk.Entry(root)
entry_altura.grid(row=5,column=2,padx=5,pady=5,sticky="we")

label_peso = tk.Label(root, text="Peso(kg): ") 
label_peso.grid(row=6,column=1,padx=5,pady=5,sticky="ee")
entry_peso = tk.Entry(root)
entry_peso.grid(row=6,column=2,padx=5,pady=5,sticky="we")

button = tk.Button(root,text="Enviar")
button.grid(row=7,column=2,padx=5,pady=5, sticky="we", columnspan=2)

def mostrar_infos():
    messagebox.showinfo("Iformações", f"Nome: {entry_nome.get()}\n ")

button.config(command=mostrar_infos)



root.mainloop()