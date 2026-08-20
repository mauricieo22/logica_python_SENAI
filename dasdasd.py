import tkinter as tk

def apagar_label():
    # Opção 1: Limpar o texto
    lbl_mensagem.config(text="")
    
    # Opção 2: Destruir o componente completamente (remova o comentário abaixo)
    # lbl_mensagem.destroy()

def mostrar_mensagem():
    # Define o texto e agenda para sumir após 3000 ms (3 segundos)
    lbl_mensagem.config(text="Operação realizada com sucesso!")
    root.after(3000, apagar_label)

root = tk.Tk()
root.title("Exemplo de Tempo no Label")
root.geometry("400x200")

btn_mostrar = tk.Button(root, text="Mostrar Mensagem", command=mostrar_mensagem)
btn_mostrar.pack(pady=20)

lbl_mensagem = tk.Label(root, text="", fg="green", font=("Arial", 12))
lbl_mensagem.pack(pady=20)

root.mainloop()
