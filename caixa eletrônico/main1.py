import tkinter as tk
from tkinter import ttk,Canvas

USUARIOS = {
    "0001": "0001"

}

def verificar_login():
    usuario_digitado = entry_conta.get()
    senha_digitada = entry_conta.get()
    
    # Usuário e senha corretos (exemplo fictício)
    usuario_correto = "admin"
    senha_correta = "1234"
    
    if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        janela.destroy() # Fecha a tela de login após o sucesso
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

root = tk.Tk()
root.title("Calculadora de resistor")
root.geometry("800x500")
root.config(bg="white")

root = tk.Tk()
root.title("Bem vindo ao Caixa Eletrônico")
root.geometry("800x500")
root.config(bg="#dbfd42")

canvas = Canvas(root, width=800, height= 500 , bg="#0003be")

canvas.create_rectangle(20,80,780,480, fill= "white", outline= "white")

titulo = tk.Label(root, text="Bem vindo ao Caixa Eletrônico!", font=("Arial", 20, "bold",),bg="#ec6211", fg="white")
titulo.place(x= 175, y= 30)



#login do cliente
def login():

    label_1 = tk.Label(root, text="             \n", font=("Arial", 60,"bold"), bg="white",anchor="w")
    label_1.place(x= 250, y= 140)

    label_conta = tk.Label(root, text="Digite sua conta: ", font=("Arial", 22,"bold"), bg="white",anchor="w")
    label_conta.place(x= 250, y= 140)

    entry_conta = tk.Entry(root)
    entry_conta.place(x= 310, y= 190)

    label_senha = tk.Label(root, text="Digite sua senha: ", font=("Arial", 22,"bold"), bg="white", anchor="w")
    label_senha.place(x= 250, y= 290)

    entry_senha = tk.Entry(root)
    entry_senha.place(x= 310, y= 190)


#botão incial do programa
botao_comecar = tk.Button(root,command=login ,text="Começar", font=("Arial", 40,"bold"), fg= "white", bg="#ec6211", anchor="center")
botao_comecar.place(x= 255, y= 210)





canvas.pack()
root.mainloop()