import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

ARQUIVO = "contas.json"

#DADOS
if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        contas = json.load(arquivo)
else:
    contas = {}

conta_atual = ""
saldo = 0

AZUL = "#0878A8"
AZUL_ESCURO = "#07578A"
AZUL_BOTAO = "#F2F6F7"
LARANJA = "#F6A800"
BRANCO = "#FFFFFF"
CINZA = "#DCECEF"


def salvar():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(contas, arquivo, indent=4)


#JANELA
janela = tk.Tk()
janela.title("Caixa Eletrônico")
janela.geometry("900x600")
janela.resizable(False, False)

canvas = tk.Canvas(
    janela,
    width=900,
    height=600,
    bg=AZUL,
    highlightthickness=0
)
canvas.pack()


def limpar():
    canvas.delete("all")


def seta(x, y, lado="esquerda"):
    """Desenha uma seta simples."""
    if lado == "esquerda":
        pontos = [x + 18, y, x, y + 15, x + 18, y + 30]
    else:
        pontos = [x, y, x + 18, y + 15, x, y + 30]

    canvas.create_polygon(
        pontos,
        fill=AZUL_ESCURO,
        outline=AZUL_ESCURO
    )


def botao(texto, x, y, comando, lado="esquerda", destaque=False):
    largura = 370
    altura = 58

    #borda laranja quando selecionado
    if destaque:
        canvas.create_rectangle(
            x - 4, y - 4,
            x + largura + 4, y + altura + 4,
            fill=LARANJA,
            outline=LARANJA
        )

    canvas.create_rectangle(
        x, y,
        x + largura, y + altura,
        fill=AZUL_BOTAO,
        outline=AZUL_BOTAO
    )

    if lado == "esquerda":
        seta(x + 15, y + 14, "esquerda")
        canvas.create_text(
            x + 48, y + 29,
            text=texto,
            anchor="w",
            fill=AZUL_ESCURO,
            font=("Arial", 15, "bold")
        )
    else:
        seta(x + largura - 33, y + 14, "direita")
        canvas.create_text(
            x + largura - 48, y + 29,
            text=texto,
            anchor="e",
            fill=AZUL_ESCURO,
            font=("Arial", 15, "bold")
        )

    #área clicável
    tag = "botao_" + texto.replace(" ", "_")
    canvas.create_rectangle(
        x, y,
        x + largura, y + altura,
        fill="",
        outline="",
        tags=(tag,)
    )

    canvas.tag_bind(
        tag,
        "<Button-1>",
        lambda evento: comando()
    )

    canvas.tag_bind(
        tag,
        "<Enter>",
        lambda evento: canvas.config(cursor="hand2")
    )

    canvas.tag_bind(
        tag,
        "<Leave>",
        lambda evento: canvas.config(cursor="")
    )


#MENU
def mostrar_menu():
    limpar()

    #fundo com detalhes decorativos
    canvas.create_polygon(
        0, 0, 180, 0, 0, 180,
        fill="#096C99",
        outline=""
    )

    canvas.create_polygon(
        0, 600, 190, 600, 0, 410,
        fill=LARANJA,
        outline=""
    )

    canvas.create_polygon(
        900, 600, 700, 600, 900, 400,
        fill="#0A6B94",
        outline=""
    )

    #título
    canvas.create_text(
        450, 35,
        text="Use os botões abaixo da tela",
        fill=BRANCO,
        font=("Arial", 22, "bold")
    )

    #informação da conta
    canvas.create_text(
        450, 75,
        text=f"Conta: {conta_atual}   |   Saldo: R$ {saldo},00",
        fill=BRANCO,
        font=("Arial", 13, "bold")
    )

    #botões no mesmo estilo da imagem
    botao(
        "CONSULTAR SALDO",
        45, 120,
        consultar,
        "esquerda"
    )

    botao(
        "SACAR",
        485, 120,
        sacar,
        "direita"
    )

    botao(
        "DEPOSITAR",
        45, 205,
        depositar,
        "esquerda"
    )

    botao(
        "SAIR",
        485, 205,
        sair,
        "direita"
    )

    #area de informaçoes
    canvas.create_rectangle(
        45, 310, 855, 500,
        fill="#EAF1F3",
        outline="#EAF1F3"
    )

    canvas.create_text(
        450, 350,
        text="CAIXA ELETRÔNICO",
        fill=AZUL_ESCURO,
        font=("Arial", 24, "bold")
    )

    canvas.create_text(
        450, 395,
        text="Escolha uma das opções acima",
        fill=AZUL_ESCURO,
        font=("Arial", 17)
    )

    canvas.create_text(
        450, 435,
        text="Use os botões para realizar suas operações.",
        fill=AZUL_ESCURO,
        font=("Arial", 14)
    )

    canvas.create_text(
        450, 475,
        text="Saldo inicial de uma conta nova: R$ 1.000,00",
        fill=AZUL_ESCURO,
        font=("Arial", 13)
    )


#operações
def consultar():
    messagebox.showinfo(
        "SALDO E EXTRATO",
        f"Seu saldo atual é:\n\nR$ {saldo},00"
    )


def depositar():
    global saldo

    valor = simpledialog.askstring(
        "DEPOSITAR",
        "Digite o valor inteiro para depósito:",
        parent=janela
    )

    if valor is None:
        return

    if not valor.isdigit() or int(valor) <= 0:
        messagebox.showerror(
            "ERRO",
            "Digite somente um valor inteiro positivo."
        )
        return

    valor = int(valor)
    saldo += valor

    contas[conta_atual]["saldo"] = saldo
    salvar()
    mostrar_menu()

    messagebox.showinfo(
        "DEPÓSITO",
        f"Depósito realizado com sucesso!\n\n"
        f"Saldo atual: R$ {saldo},00"
    )


def sacar():
    global saldo

    valor = simpledialog.askstring(
        "SAQUE",
        "Digite o valor inteiro para saque:",
        parent=janela
    )

    if valor is None:
        return

    if not valor.isdigit() or int(valor) <= 0:
        messagebox.showerror(
            "ERRO",
            "Digite somente um valor inteiro positivo."
        )
        return

    valor = int(valor)

    if valor > saldo:
        messagebox.showerror(
            "ERRO",
            "Saldo insuficiente."
        )
        return

    #calcula as cédulas
    restante = valor
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    texto = ""

    for cedula in cedulas:
        quantidade = restante // cedula

        if quantidade > 0:
            texto += f"{quantidade} cédula(s) de R$ {cedula}\n"
            restante %= cedula

    saldo -= valor
    contas[conta_atual]["saldo"] = saldo
    salvar()
    mostrar_menu()

    messagebox.showinfo(
        "SAQUE REALIZADO",
        f"Saque realizado com sucesso!\n\n"
        f"Entregar:\n{texto}\n"
        f"Saldo atual: R$ {saldo},00"
    )


def sair():
    salvar()
    janela.destroy()


#login
def login():
    global conta_atual, saldo

    conta = simpledialog.askstring(
        "CONTA",
        "Digite sua conta:",
        parent=janela
    )

    if not conta:
        return

    senha = simpledialog.askstring(
        "SENHA",
        "Digite sua senha:",
        show="*",
        parent=janela
    )

    if not senha:
        return

    #conta nova. Começa com R$ 1.000,00
    if conta not in contas:
        contas[conta] = {
            "senha": senha,
            "saldo": 1000
        }
        salvar()

    conta_atual = conta
    saldo = contas[conta]["saldo"]

    mostrar_menu()


#tela inicial
def tela_inicial():
    limpar()

    canvas.create_polygon(
        0, 0, 180, 0, 0, 180,
        fill="#096C99",
        outline=""
    )

    canvas.create_polygon(
        0, 600, 190, 600, 0, 410,
        fill=LARANJA,
        outline=""
    )

    canvas.create_text(
        450, 80,
        text="CAIXA ELETRÔNICO",
        fill=BRANCO,
        font=("Arial", 32, "bold")
    )

    canvas.create_text(
        450, 125,
        text="Use os botões para acessar sua conta",
        fill=BRANCO,
        font=("Arial", 17)
    )

    canvas.create_rectangle(
        150, 180, 750, 500,
        fill="#EAF1F3",
        outline="#EAF1F3"
    )

    canvas.create_text(
        450, 225,
        text="BEM-VINDO",
        fill=AZUL_ESCURO,
        font=("Arial", 26, "bold")
    )

    # Botão entrar
    canvas.create_rectangle(
        270, 290, 630, 350,
        fill=AZUL_ESCURO,
        outline=AZUL_ESCURO
    )

    canvas.create_text(
        450, 320,
        text="ENTRAR",
        fill=BRANCO,
        font=("Arial", 30, "bold")
    )

    canvas.create_rectangle(
        270, 290, 630, 350,
        fill="",
        outline="",
        tags=("entrar",)
    )

    canvas.tag_bind(
        "entrar",
        "<Button-1>",
        lambda evento: login()
    )

    canvas.tag_bind(
        "entrar",
        "<Enter>",
        lambda evento: canvas.config(cursor="hand2")
    )

    canvas.tag_bind(
        "entrar",
        "<Leave>",
        lambda evento: canvas.config(cursor="")
    )



tela_inicial()

janela.protocol("WM_DELETE_WINDOW", sair)
janela.mainloop()
