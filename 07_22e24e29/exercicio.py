#Calculadora de IMC

#Requisitos:
# 1 Widgets Básicos  -  Use Label, Entry e Button.
# 2 Campo de Entrada - Dois Entry: peso (kg) e altura (m).
# 3 Botão Calcular - Botão que calcula o IMC e exibe e, um Label
# 4 Faixa IMC -  Exibir mensagem: Abaixo do peso, Saudável, Sobrepeso ou Obesidade.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")


label_peso = tk.Label(root, text="Seu peso(kg):")
entry_peso = tk.Entry(root)
label_altura = tk.Label(root, text="Sua altura(m):")
entry_altura = tk.Entry(root)


def button_command():
    messagebox.showinfo("Resultado")

button = tk.Button(root,text="Calcular",command=button_command)

label_peso.pack()
entry_peso.pack()
label_altura.pack()
entry_altura.pack()
button.pack()

root.mainloop()