import tkinter as tk

#Cria a janela principal   
root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")

#Cria um rótulo (label) com o texto "Hello World!"
message = tk.Label(root, text=("Primeira mensagem.\n"))

message2 = tk.Label(root, text=("Segunda mensagem."))

#posiciona o rótulo na janela
message.pack()
message2.pack()

root.geometry("400x200+700+350")

#inicia o loop principal da interface gráfica
root.mainloop()