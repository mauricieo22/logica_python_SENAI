import tkinter as tk
from tkinter import ttk, Image, Label
import random
#pip install Pillow
import PIL
from PIL import ImageTk, Image


#cores--------------------------
cor0 = "#FFFFFF" # white / branca
cor1 = "#333333" # black / preta
cor2 = "#fcc058" # orange / laranja
cor3 = "#ffff00" # yellow / amarela
cor4 = "#00ff00" # green / verde
cor5 = "#e85151" # red / vermelha
fundo= "#3b3b3b" # grey / cinza

janela = tk.Tk()
janela.title("Pedra, Papel e Tesoura")
janela.geometry("260x280")
janela.configure(bg=fundo)

frame_cima = tk.Frame(width=260, height=100, bg=cor1,relief="raised")
frame_cima.grid(row=0,column=0,sticky="nw")

frame_baixo = tk.Frame(width=260, height=300,bg=cor0,relief="flat")
frame_baixo.grid(row=1,column=0, sticky="nw")

#configurando os jogadores

#jogador pessoa
app_pessoa = tk.Label(frame_cima, text="Jogador", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pessoa.place(x=33, y=70)

#barra marcou pontos Pessoa
app_pessoa_linha = tk.Label(frame_cima, text="", height=10, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pessoa_linha.place(x=0, y=0)

#pontuação pessoa
app_pessoa_pontos = tk.Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pessoa_pontos.place(x=50, y=20)

#separação da pontuação
app_vs = tk.Label(frame_cima, text=":", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_vs.place(x=125, y=20)

#jogador PC
app_pc= tk.Label(frame_cima, text="PC", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pc.place(x=182, y=70)

#barra marcou pontos PC
app_pc_linha = tk.Label(frame_cima, text="", height=10, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pc_linha.place(x=255, y=0)

#pontuação pc
app_pc_pontos = tk.Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pc_pontos.place(x=180, y=20)

#barra empate
barra_empate = tk.Frame(width=260, height=5,bg=cor1,relief="raised")
barra_empate.place(x=0, y=95)

#mostra a jogada do jogador
app_jogada_pessoa = tk.Label(frame_baixo, text="", height=1, anchor="center",
                           bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pessoa.place (x=10, y=10)

#mostra a jogada do PC
app_jogada_pc = tk.Label(frame_baixo, text="", height=1, anchor="center",
                           bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pc.place (x=180, y=10)
 
    
global escolha_pessoa
global escolha_pc
global pontos_pessoa
global pontos_pc
global rodadas
pontos_pessoa = 0
pontos_pc = 0
rodadas = 5


def jogar(jogada):
    global pontos_pessoa
    global pontos_pc
    global rodadas
    opcoes = ["pedra", "papel", "tesoura"]

    app_pc_linha["bg"] = cor1
    app_pessoa_linha["bg"] = cor1
    barra_empate["bg"] = cor1


    if rodadas > 0:
        print(rodadas)
        escolha_pc = random.choice(opcoes)
        app_jogada_pc["text"] = escolha_pc

        escolha_pessoa = jogada
        app_jogada_pessoa["text"] = escolha_pessoa
        print(escolha_pessoa, escolha_pc)
        rodadas -= 1

        def testa_empate():
            if escolha_pessoa == escolha_pc:
                return True
            else:
                return False
            
        if testa_empate():
            barra_empate["bg"] = cor2
        #caso vitória da rodada pessoa
        elif (escolha_pessoa == "pedra" and escolha_pc == "tesoura") or (escolha_pessoa == "papel" and escolha_pc == "pedra") or (escolha_pessoa == "tesoura" and escolha_pc == "papel"):
            pontos_pessoa += 10
            app_pessoa_linha["bg"] = cor4
    #caso vitória da rodada PC
        else:
            pontos_pc += 10
            app_pc_linha["bg"] = cor5

    elif rodadas == 0:
        verificar_vencedor()

    app_pessoa_pontos["text"] = pontos_pessoa
    app_pc_pontos["text"] = pontos_pc


def iniciar_jogo():
    global icone_pedra
    global icone_papel
    global icone_tesoura
    global btn_pedra
    global btn_papel
    global btn_tesoura
    global botao_jogar

    #botão pedra
    icone_pedra = PIL.Image.open("pedra.png")
    icone_pedra = icone_pedra.resize((50,50), PIL.Image.Resampling.LANCZOS)
    icone_pedra = PIL.ImageTk.PhotoImage(icone_pedra)
    btn_pedra = tk.Button(frame_baixo,command=lambda: jogar("pedra"), width=50, height=50, image=icone_pedra, compound="center", bg=cor0, fg=cor0, font=("Ivy 10 bold"), anchor="center", relief="flat")
    btn_pedra.place(x=15, y=60)

    #botão papel
    icone_papel = PIL.Image.open("papel.png")
    icone_papel = icone_papel.resize((50,50), PIL.Image.Resampling.LANCZOS)
    icone_papel = PIL.ImageTk.PhotoImage(icone_papel)
    btn_papel = tk.Button(frame_baixo,command=lambda: jogar("papel"), width=50, height=50, image=icone_papel, compound="center", bg=cor0, fg=cor0, font=("Ivy 10 bold"), anchor="center", relief="flat")
    btn_papel.place(x=100, y=60)

    #botão tesoura
    icone_tesoura = PIL.Image.open("tesoura.png")
    icone_tesoura = icone_tesoura.resize((50,50), PIL.Image.Resampling.LANCZOS)
    icone_tesoura = PIL.ImageTk.PhotoImage(icone_tesoura)
    btn_tesoura = tk.Button(frame_baixo,command=lambda: jogar("tesoura"), width=50, height=50, image=icone_tesoura, compound="center", bg=cor0, fg=cor0, font=("Ivy 10 bold"), anchor="center", relief="flat")
    btn_tesoura.place(x=190, y=60)

#botão "jogar"
botao_jogar = tk.Button(text="Jogar",command=iniciar_jogo, width=24, height=1,anchor="center", bg=cor1, fg=cor0, font=("Arial", 12, "bold"))
botao_jogar.place(x=4, y=243,)

#LABEL QUE MOSTRA QUEM GANHOU O JOGO
vencedor = tk.Label(frame_baixo, text="", height=1, bg=cor0, fg=cor1, font=("Ivy 17 bold"))
vencedor.place(x=0, y=0, width=260, height=40)

#VERFICAR QUEM GANHOU O JOGO
def verificar_vencedor():
    if pontos_pessoa > pontos_pc:
        vencedor["text"] = "JOGADOR 1 GANHOU!"
        vencedor["bg"] = cor4
        vencedor["fg"] = cor1

    elif pontos_pessoa < pontos_pc:
        vencedor["text"] = "PC GANHOU!"
        vencedor["bg"] = cor5
        vencedor["fg"] = cor1

    else:
        vencedor["text"] = "EMPATE!"
        vencedor["bg"] = cor3
        vencedor["fg"] = cor1


#REINICIAR O JOGO
    def reiniciar_jogo():
        global pontos_pessoa
        global pontos_pc
        global rodadas
        pontos_pessoa = 0
        pontos_pc = 0
        rodadas = 5

        app_pessoa_pontos["text"] = "0"
        app_pc_pontos["text"] = "0"
        app_jogada_pessoa["text"] = ""
        app_jogada_pc["text"] = ""
        app_pessoa_linha["bg"] = cor1
        app_pc_linha["bg"] = cor1
        barra_empate["bg"] = cor1
        vencedor["fg"] = cor0
        vencedor["bg"] = cor0
        botao_jogar_novamente["text"] = "Jogar"
       

    botao_jogar_novamente = tk.Button(text="Jogar novamente",command=reiniciar_jogo, width=24, height=1,anchor="center", bg=cor1, fg=cor0, font=("Arial", 12, "bold"))
    botao_jogar_novamente.place(x=4, y=243)

janela.mainloop()