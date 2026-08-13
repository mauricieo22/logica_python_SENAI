import tkinter as tk
from tkinter import ttk, Image, ImageTk

#pip install Pillow
from PIL import Image

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

frame_baixo = tk.Frame(width=260, height=300,relief="flat")
frame_baixo.grid(row=1,column=0, sticky="nw")

#configurando os jogadores

#jogador pessoa
app_pessoa = tk.Label(frame_cima, text="Jogador", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pessoa.place(x=10, y=70)

#barra marcou pontos
app_pessoa_linha = tk.Label(frame_cima, text="", height=10, anchor="center", bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_pessoa_linha.place(x=0, y=0)

#pontuação pessoa
app_pessoa_pontos = tk.Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pessoa_pontos.place(x=50, y=20)

#separação da pontuação
app_vs = tk.Label(frame_cima, text=":", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_vs.place(x=125, y=20)

#jogador PC
app_pc= tk.Label(frame_cima, text="PC", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 10 bold"))
app_pc.place(x=200, y=70)

#barra marcou pontos PC
app_pc_linha = tk.Label(frame_cima, text="", height=10, anchor="center", bg=cor4, fg=cor0, font=("Ivy 10 bold"))
app_pc_linha.place(x=255, y=0)

#pontuação pc
app_pc_pontos = tk.Label(frame_cima, text="0", height=1, anchor="center", bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pc_pontos.place(x=180, y=20)

#barra empate
barra_empate = tk.Frame(width=255, height=5,bg=cor2,relief="raised")
barra_empate.place(x=0, y=95)

#configurando o frame baixo
icone_pedra = Image.open("./images/pedra.png")
icone_pedra = icone_pedra.resize((50,50), Image.Resampling.LANCZOS)
icone_pedra =   ImageTk.PhotoImage(icone_pedra)
btn_pedra = tk.Button(frame_baixo, width=50, height=50, image=icone_pedra, compound="center", bg=cor0, fg=cor0, font=("Ivy 10 bold"), anchor="center", relief="flat")
btn_pedra.place(x=15, y=60)

janela.mainloop()