import tkinter as tk
from tkinter import ttk,Canvas

root = tk.Tk()
root.title("Calculadora de resistor")
root.geometry("800x500")
root.config(bg="white")

canvas = Canvas(root, width=800, height= 500 , bg="#c1cdcd")

canvas.create_rectangle(20,80,780,480, fill= "white", outline= "white")

titulo = tk.Label(root, text="Calculadora de resistor", font=("Arial", 20, "bold"),bg="#c1cdcd")
titulo.place(x= 20, y= 30)


info_ask = tk.Label(root, text="Como deseja informar o resistor?", font=("Arial", 10, "bold"),bg="#c1cdcd")
info_ask.place(x= 30, y= 90)



#MODO POR CORES

def info_cores():
    global faixa1, combobox_faixa_1, faixa2, combobox_faixa_2, multiplicador, combobox_multiplicador, tolerancia, combobox_tolerancia, btn_calcular, label_info

    faixa1 = tk.Label(root, text="Faixa 1:", font=("Arial", 10,"bold"), bg="white")
    faixa1.place(x= 30, y= 160)
    combobox_faixa_1 = ttk.Combobox(root, values = ["Selecione uma cor","Preto (0)","Marrom (1)","Vermelho (2)","Laranja (3)","Amarelo (4)","Verde (5)","Azul (6)", "Violeta (7)","Cinza (8)", "Branco (9)"])
    combobox_faixa_1.place(x= 30, y= 190)

    faixa2 = tk.Label(root, text="Faixa 2:", font=("Arial", 10,"bold"), bg="white")
    faixa2.place(x=200, y= 160)
    combobox_faixa_2 = ttk.Combobox(root, values = ["Selecione uma cor","Preto (0)","Marrom (1)","Vermelho (2)","Laranja (3)","Amarelo (4)","Verde (5)","Azul (6)", "Violeta (7)","Cinza (8)", "Branco (9)"])
    combobox_faixa_2.place(x= 200, y= 190)

    multiplicador = tk.Label(root, text="Multiplicador:", font=("Arial", 10,"bold"), bg="white")
    multiplicador.place(x=370, y= 160)
    combobox_multiplicador = ttk.Combobox(root, values = ["Selecione uma cor","Prata (0.01Ω)","Ouro (0.1Ω)","Preto (1Ω)","Marrom (10Ω)","Vermelho (100Ω)","Laranja (1000Ω)","Amarelo (10000Ω)","Verde (100000Ω)","Azul (1000000Ω)", "Violeta (10000000Ω)"])
    combobox_multiplicador.place(x= 370, y= 190)

    tolerancia = tk.Label(root, text="Tolerância:", font=("Arial", 10,"bold"), bg="white")
    tolerancia.place(x=540, y= 160)
    combobox_tolerancia = ttk.Combobox(root, values = ["Selecione uma cor","Prata (±5%)","Ouro (±10%)","Preto (±20%)","Marrom (±1%)","Vermelho (±2%)","Verde (±0.1%)","Azul (±0.25%)", "Violeta (±0.1%)"])
    combobox_tolerancia.place(x= 540, y= 190) 


    btn_calcular = tk.Button(root, text="Calcular resistência", font=("Arial", 14,"bold"), fg= "black", bg="#7fffd4")
    btn_calcular.place(x= 30, y= 230)

    label_info = tk.Label(root, text="Digite o valor da resistência ou selecione as cores", font=("Arial", 9,"bold"), bg="white")
    label_info.place(x= 30, y= 270)

    canvas.create_rectangle(30,295,770,470, fill= "#c1cdcd", outline= "white")

    canvas.create_text(400,375, text="AGUARDE A SELEÇÃO DO MODO", font=("Arial", 12,"italic", "bold"), fill= "white")


#MODO POR VALOR

def info_valor():
    global valor_resistencia,entry_valor,tolerancia2,combobox_tolerancia2

    valor_resistencia = tk.Label(root, text="Valor da resistêcia (Ω):", font=("Arial", 10,"bold"), bg="white")
    valor_resistencia.place(x= 30, y= 160)
    
    entry_valor = tk.Entry(root,bg="white")
    entry_valor.insert(0," ")
    entry_valor.pack()
    entry_valor.place(x= 30, y= 190)

    tolerancia2 = tk.Label(root, text="Tolerância:", font=("Arial", 10,"bold"), bg="white")
    tolerancia2.place(x=200, y= 160)

    combobox_tolerancia2 = ttk.Combobox(root, values = ["Prata (±5%)","Ouro (±10%)","Preto (±20%)","Marrom (±1%)","Vermelho (±2%)","Verde (±0.1%)","Azul (±0.25%)", "Violeta (±0.1%)"])
    combobox_tolerancia2.place(x= 200, y= 188)

    btn_calcular = tk.Button(root, text="Calcular cores", font=("Arial", 14,"bold"), fg= "black", bg="#7fffd4")
    btn_calcular.place(x= 30, y= 230)

    label_info = tk.Label(root, text="Digite o valor da resistência ou selecione as cores", font=("Arial", 9,"bold"), bg="white")
    label_info.place(x= 30, y= 270)

    canvas.create_rectangle(30,295,770,470, fill= "#c1cdcd", outline= "white")

    canvas.create_text(400,375, text="AGUARDE A SELEÇÃO DO MODO", font=("Arial", 12,"italic", "bold"), fill= "white")


            
def trocar_modo():
    if Radiobutton_estado.get() == 1:

        info_valor()
    elif Radiobutton_estado.get() == 2:
        info_cores()
    


Radiobutton_estado = tk.IntVar()

info_valor = tk.Radiobutton(root, command=info_valor, text="Informar por valor", variable=Radiobutton_estado, value=1,bg="#c1cdcd")
info_valor.place(x= 30, y= 125)
info_cores = tk.Radiobutton(root,command=info_cores, text="Informar por cores", variable=Radiobutton_estado, value=2,bg="#c1cdcd")
info_cores.place(x= 200, y= 125)










canvas.pack()
root.mainloop()