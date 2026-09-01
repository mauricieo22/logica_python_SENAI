import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculadora de resistor")
root.geometry("800x500")
root.config(bg="grey")


tk.Label(root, text="\nCalculadora de Resistor",bg= "grey",fg= "white", font=("Arial", 17, "bold")).grid(row=4, column=0, sticky="e")


# cor0 = "#333333" #Preto
# cor1 =  #Marrom
# cor2 = "#e85151" #Vermelho
# cor3 = "#fcc058" #Laranja
# cor4 = "#ffff00" #Amarelo
# cor5 = "#00ff00" #Verde
# cor6 = #Azul
# cor7 = #Violeta
# cor8 = #Cinza
# cor9 = #Branco


# fundo= "#3b3b3b" # grey / cinza



# #cores e valores das faixas
# cores = {
#     "Preto" = 0,
#     "Marrom" = 1,
#     "Vermelho" = 2,
#     "Laranja" = 3,
#     "Amarelo" = 4,
#     "Verde" = 5,
#     "Azul" = 6,
#     "Violeta" = 7,
#     "Cinza" = 8,
#     "Branco"= 9
# }

# #multiplicadores e seus valores
# multiplicadores = {
#     "Prata" = 0.01
#     "Ouro" = 0.1
#     "Preto" = 1
#     "Marrom" = 10
#     "Vermelho" = 100
#     "Laranja" = 1000
#     "Amarelo" = 10000
#     "Verde" = 100000
#     "Azul" = 1000000
#     "Violeta" = 10000000
#  }

tk.Label(root, text="Como deseja informar o resistor?", font=("Arial", 10, "bold")).grid(row=10,column=0,padx=5,pady=5)



tk.Label(root, text="Faixa 1:", font=("Arial", 10)).grid(row=14,column=0,padx=5,pady=5)

combobox_faixa_1 = ttk.Combobox(root, values = ["Prata","Ouro","Preto","Marrom","Vermelho","Laranja","Amarelo","Verde","Azul", "Violeta"])
combobox_faixa_1.grid(row=15,column=0,padx=0,pady=5)




 

root.mainloop()