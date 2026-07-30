#Calculadora de IMC

#Requisitos:
# 1 Widgets Básicos  -  Use Label, Entry e Button.
# 2 Campo de Entrada - Dois Entry: peso (kg) e altura (m).
# 3 Botão Calcular - Botão que calcula o IMC e exibe e, um Label
# 4 Faixa IMC -  Exibir mensagem: Abaixo do peso, Saudável, Sobrepeso ou Obesidade.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("400x150")


label_peso = tk.Label(root, text="Seu peso(kg):")
entry_peso = tk.Entry(root)
label_altura = tk.Label(root, text="Sua altura(cm):")
entry_altura = tk.Entry(root)

def calcular_imc():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get()) / 100
    return peso / (altura ** 2)

def faixa_imc():
    imc = calcular_imc()
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Saudável"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def button_command():
    label = tk.Label(root, text=f"Seu IMC é: {calcular_imc():.2f} \n ({faixa_imc()})")
    label.pack()

button = tk.Button(root,text="Calcular",command=button_command)

label_peso.pack()
entry_peso.pack()
label_altura.pack()
entry_altura.pack()
button.pack()


root.mainloop()