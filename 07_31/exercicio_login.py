#Tela de Login - PACK

#O que esse projeto demonstra

# Uma tela de login completa cnstruída apenas com o geometry manager pack e seus parâmentros.

# anchor = "w" alinha os labels "Usuário" e "Senha" à esquerda.
# side = "left" e side = "right" posicionam os elementos no rodapé.
# fill = "x" no título faz o Label ocupar toda a largura.
# ipady = 5 aumenta a altura interna do título.

import tkinter as tk
from tkinter import  PhotoImage, messagebox

root = tk.Tk()
root.title("TELA DE LOGIN") #título da janela
root.geometry("400x500")         #tamanho da janela

label_login = tk.Label(root, text="Faça seu login", font=("Arial",42))
label_login.pack(padx=10, pady=10, fill="x", ipady=5, anchor="w") #título da tela de login

imagem_login = PhotoImage(file="user.png")
label_imagem = tk.Label(root, image=imagem_login, bg="white", width=200, height=200)
label_imagem.pack()

label_usuario = tk.Label(root, text="Usuário:") 
label_usuario.pack(anchor="w", padx=20)
entry_usuario = tk.Entry(root)
entry_usuario.pack()

label_senha = tk.Label(root, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(root)
entry_senha.pack()

button = tk.Button(root,text="Entrar")
button.pack()

checkbox = tk.Checkbutton(root, text= "Lembrar de mim", font=("Arial",9))
checkbox.deselect()
checkbox.pack(side="left")

label_esqueceu = tk.Label(root, text="Esqueceu sua senha?", font=("Arial",9))
label_esqueceu.pack(side="right")

root.mainloop()