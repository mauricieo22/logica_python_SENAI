import tkinter as tk
from tkinter import messagebox, simpledialog

# [conta, senha, saldo]
usuarios = [
    ["1234", "1234", 1000],
    ["1111", "1111", 1000],
    ["2222", "2222", 1000]
]

conta = ""
saldo = 0

# ---------------- JANELA ----------------
janela = tk.Tk()
janela.title("Caixa Eletrônico")
janela.geometry("700x500")
janela.resizable(False, False)

tela = tk.Canvas(
    janela,
    width=700,
    height=500,
    bg="#0878A8"
)
tela.pack()


def limpar():
    tela.delete("all")


# ---------------- LOGIN ----------------
def login():
    global conta, saldo

    conta_digitada = entrada_conta.get()
    senha_digitada = entrada_senha.get()

    # Procura a conta na lista
    for usuario in usuarios:
        if usuario[0] == conta_digitada and usuario[1] == senha_digitada:
            conta = usuario[0]
            saldo = usuario[2]
            menu()
            return

    messagebox.showerror(
        "Erro",
        "Conta ou senha incorreta."
    )


def tela_login():
    limpar()

    tela.create_text(
        350, 55,
        text="CAIXA ELETRÔNICO",
        fill="white",
        font=("Arial", 26, "bold")
    )

    tela.create_text(
        350, 95,
        text="Digite seus dados para entrar",
        fill="white",
        font=("Arial", 15)
    )

    tela.create_rectangle(
        150, 135, 550, 430,
        fill="#EAF1F3",
        outline="#EAF1F3"
    )

    tela.create_text(
        350, 175,
        text="ENTRAR",
        fill="#075A8C",
        font=("Arial", 22, "bold")
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


# ---------------- MENU ----------------
def criar_botao(texto, x, y, funcao):
    tela.create_rectangle(
        x, y, x + 300, y + 55,
        fill="white",
        outline="white"
    )

    tela.create_text(
        x + 150, y + 28,
        text=texto,
        fill="#075A8C",
        font=("Arial", 14, "bold")
    )

    tag = "botao" + str(x) + str(y)

    tela.create_rectangle(
        x, y, x + 300, y + 55,
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

    entrada_conta.destroy()
    entrada_senha.destroy()

    tela.create_text(
        350, 40,
        text="CAIXA ELETRÔNICO",
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
        "◀  CONSULTAR SALDO",
        30, 120,
        consultar
    )

    criar_botao(
        "SACAR  ▶",
        370, 120,
        sacar
    )

    criar_botao(
        "◀  DEPOSITAR",
        30, 200,
        depositar
    )

    criar_botao(
        "SAIR  ▶",
        370, 200,
        sair
    )

    tela.create_text(
        350, 330,
        text="Conta: " + conta,
        fill="white",
        font=("Arial", 16, "bold")
    )

    tela.create_text(
        350, 365,
        text=f"Saldo: R$ {saldo},00",
        fill="white",
        font=("Arial", 16)
    )


# ---------------- OPERAÇÕES ----------------
def consultar():
    messagebox.showinfo(
        "Saldo",
        f"Seu saldo é R$ {saldo},00"
    )


def atualizar_saldo():
    # Atualiza o saldo na lista
    for usuario in usuarios:
        if usuario[0] == conta:
            usuario[2] = saldo


def depositar():
    global saldo

    valor = simpledialog.askinteger(
        "Depósito",
        "Digite o valor:"
    )

    if valor is None or valor <= 0:
        return

    saldo += valor
    atualizar_saldo()

    messagebox.showinfo(
        "Depósito",
        f"Depósito realizado!\nSaldo: R$ {saldo},00"
    )

    menu()


def sacar():
    global saldo

    valor = simpledialog.askinteger(
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

    restante = valor
    cedulas = ""

    # Calcula as cédulas
    for cedula in [100, 50, 20, 10, 5, 2, 1]:
        quantidade = restante // cedula

        if quantidade > 0:
            cedulas += f"{quantidade} cédula(s) de R$ {cedula}\n"
            restante = restante % cedula

    saldo -= valor
    atualizar_saldo()

    messagebox.showinfo(
        "Saque",
        f"Saque realizado!\n\n"
        f"Entregar:\n{cedulas}\n"
        f"Saldo: R$ {saldo},00"
    )

    menu()


def sair():
    janela.destroy()


# ---------------- INÍCIO ----------------
tela_login()
janela.mainloop()
