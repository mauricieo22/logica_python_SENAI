# Calculadora de IMC

# Requisitos:
# 1 Widgets Básicos  -  Use Label, Entry e Button.
# 2 Campo de Entrada - Dois Entry: peso (kg) e altura (m).
# 3 Botão Calcular - Botão que calcula o IMC e exibe e, um Label
# 4 Faixa IMC -  Exibir mensagem: Abaixo do peso, Saudável, Sobrepeso ou Obesidade.

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculadora de IMC") #título da janela
root.geometry("400x180")         #tamanho da janela

#pede o peso
label_peso = tk.Label(root, text="Seu peso (kg):")
entry_peso = tk.Entry(root)
label_peso.pack()
entry_peso.pack()

#pede a altura
label_altura = tk.Label(root, text="Sua altura (cm):")
entry_altura = tk.Entry(root)
label_altura.pack()
entry_altura.pack()


#calcular o IMC
def calcular_imc():
    #Cria uma excessão para valores inválidos 
    try:
        peso = float(entry_peso.get().replace(",", "."))
        altura = float(entry_altura.get().replace(",", "."))
        if altura <= 0 or peso <= 0:
            raise ValueError
    except ValueError:
        labelMensagem.config(text="Informe peso e altura válidos.")


    peso = float(entry_peso.get())
    altura = float(entry_altura.get()) / 100
    return peso / (altura ** 2)


#Define a faixa do IMC
def faixa_imc():
    imc = calcular_imc()
    
    if imc < 18.5:
        mensagem =  (f"Seu IMC é {calcular_imc():.2f}\n Abaixo do peso")
    elif imc < 25:
        mensagem = (f"Seu IMC é {calcular_imc():.2f}\n Saudável")
    elif imc < 30:
        mensagem = (f"Seu IMC é {calcular_imc():.2f}\n Sobrepeso")
    elif imc < 35:
        mensagem = (f"Seu IMC é {calcular_imc():.2f}\n Obesidade")
    else:
        return (f"Seu IMC é {calcular_imc():.2f}\n Obesidade mórbida")

    labelMensagem.config(text= mensagem)
    
    
#botão de calcular
def button_command():
    faixa_imc()

button = tk.Button(root,text="Calcular",command=button_command)
button.pack()

labelMensagem = tk.Label(root, text="\nPreencha os campos e clique em Calcular.")
labelMensagem.pack()

#inicia o loop principal da interface gráfica
root.mainloop()