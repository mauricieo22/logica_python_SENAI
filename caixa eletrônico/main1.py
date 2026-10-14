import tkinter as tk
from tkinter import messagebox
import json
import os

#contas salvas com .json ao invés de um arquivo .txt
ARQUIVO = "contas.json"

#DADOS
if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r") as arquivo:
        contas = json.load(arquivo)
else:
    contas = {}

conta = ""
saldo = 0

#JANELA
janela = tk.Tk()
janela.title("Caixa Eletrônico")
janela.geometry("700x500")
janela.resizable(False, False)

tela = tk.Canvas(
    janela,
    width=700,
    height=500,
    bg="#07598C"
)
tela.pack()


def salvar():
    with open(ARQUIVO, "w") as arquivo:
        json.dump(contas, arquivo)


def limpar():
    tela.delete("all")



#LOGIN

somente_numeros = lambda s: s.isdigit()

def login():
    global conta, saldo

    conta = entrada_conta.get()
    senha = entrada_senha.get()

    if not somente_numeros(conta) or not somente_numeros(senha):
        messagebox.showwarning(
            "Atenção",
            "Digite apenas números."
        )
        return
 #se nada para conta ou senha, exibe mensagem de erro e retorna para a tela de login
    if conta == "" or senha == "":
        messagebox.showwarning(
            "Atenção",
            "Digite a conta e a senha."
        )
        return
    
    #conta nova começa com R$ 1.000
    if conta not in contas:
        contas[conta] = {
            "senha": senha,
            "saldo": 1000
        }
        salvar()

    saldo = contas[conta]["saldo"]

    menu()


def tela_login():
    limpar()

    tela.create_text(
        350, 80,
        text="CAIXA ELETRÔNICO",
        fill="white",
        font=("Arial", 26, "bold")
    )

    #painel
    tela.create_rectangle(
        150, 135, 550, 430,
        fill="#EAF1F3",
        outline="#EAF1F3"
    )

    tela.create_text(
        350, 175,
        text="Digite seus dados para entrar",
        fill="#075A8C",
        font=("Arial", 19, "bold")
    )

    tela.create_text(
        205, 225,
        text="Conta:",
        anchor="w",
        fill="#075A8C",
        font=("Arial", 14, "bold")
    )

    tela.create_text(
        205, 285,
        text="Senha:",
        anchor="w",
        fill="#075A8C",
        font=("Arial", 14, "bold")
    )

    #campos
    global entrada_conta, entrada_senha

    entrada_conta = tk.Entry(
        janela,
        font=("Arial", 15),
        width=25
    )
    entrada_conta.place(x=205, y=240)

    entrada_senha = tk.Entry(
        janela,
        font=("Arial", 15),
        width=25,
        show="*"
    )
    entrada_senha.place(x=205, y=300)

    #botão
    tela.create_rectangle(
        205, 350, 495, 405,
        fill="#075A8C",
        outline="#075A8C",
        tags="entrar"
    )

    tela.create_text(
        350, 378,
        text="ENTRAR",
        fill="white",
        font=("Arial", 15, "bold"),
        tags="entrar"
    )

    tela.tag_bind(
        "entrar",
        "<Button-1>",
        lambda evento: login()
    )

    tela.tag_bind(
        "entrar",
        "<Enter>",
        lambda evento: tela.config(cursor="hand2")
    )

    tela.tag_bind(
        "entrar",
        "<Leave>",
        lambda evento: tela.config(cursor="")
    )


#MENU
def criar_botao(texto, x, y, funcao):
    tela.create_rectangle(
        x, y, x + 280, y + 165,
        fill="white",
        outline="white"
    )

    tela.create_text(
        x + 145, y + 82,
        text=texto,
        fill="#075A8C",
        font=("Arial", 25, "bold")
    )

    tag = "botao" + str(x) + str(y)

    tela.create_rectangle(
        x, y, x + 280, y + 165,
        fill="",
        outline="",
        tags=tag
    )

    tela.tag_bind(
        tag,
        "<Button-1>",
        lambda evento: funcao()
    )


def menu():
    limpar()

     #remove os campos de login
    entrada_conta.destroy()
    entrada_senha.destroy()

    tela.create_text(
        350, 40,
        text="BEM VINDO!",
        fill="white",
        font=("Arial", 24, "bold")
    )

    tela.create_text(
        350, 75,
        text="Escolha uma opção",
        fill="white",
        font=("Arial", 15)
    )

    criar_botao(
        "CONSULTAR\n"
        "SALDO",
        40, 120,
        consultar
    )

    criar_botao(
        "SACAR",
        370, 120,
        sacar
    )

    criar_botao(
        "DEPOSITAR",
        40, 300,
        depositar
    )

    criar_botao(
        "SAIR",
        370, 300,
        sair
    )

    tela.create_text(
        350, 483,
        text="Conta: " + conta,
        fill="white",
        font=("Arial", 16)
    )


#OPERAÇÕES
def consultar():
    messagebox.showinfo(
        "Saldo",
        f"Seu saldo é R$ {saldo},00"
    )


def depositar():
    global saldo

    valor = tkinter.simpledialog.askinteger(
        "Depósito",
        "Digite o valor:"
    )

    if valor is None or valor < 2:
        messagebox.showerror(
            "Depósito inválido",
            f"Deposite um valor válido."
        )
        return

    saldo += valor
    contas[conta]["saldo"] = saldo
    salvar()

    messagebox.showinfo(
        "Depósito",
        f"Depósito realizado!\nSaldo: R$ {saldo},00"
    )

    menu()


def sacar():
    global saldo

    valor = tkinter.simpledialog.askinteger(
        "Saque",
        "Digite o valor:"
    )

    if valor is None or valor <= 0:
        return

    if valor > saldo:
        messagebox.showerror(
            "Erro",
            "Saldo insuficiente."
        )
        return
#valida a quantidade de cédulas válidas (200, 100, 50, 20, 10, 5, 2)
    if valor % 5 != 0:
        messagebox.showerror(
            "Erro!",
            "Selecione um valor com a quantidade de cédulas válidas\n"
            "(200, 100, 50, 20, 10, 5, 2)"
        )
        return
    

    restante = valor
    texto = ""

    #calcula as cédulas
    for cedula in [200, 100, 50, 20, 10, 5, 2]:
        quantidade = restante // cedula

        if quantidade > 0:
            texto += (
                f"{quantidade} cédula(s) de R$ {cedula}\n"
            )
            restante = restante % cedula

    saldo -= valor
    contas[conta]["saldo"] = saldo
    salvar()

    messagebox.showinfo(
        "Saque",
        f"Saque realizado!\n\n"
        f"Entregar:\n{texto}\n"
        f"Saldo: R$ {saldo},00"
    )

    menu()


def sair():
    salvar()
    limpar()
    tela_login()


import tkinter.simpledialog

tela_login()
janela.mainloop()
