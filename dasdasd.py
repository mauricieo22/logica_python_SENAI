import tkinter as tk
from tkinter import messagebox

# Função para mostrar a escolha
laranja_texto = "Você escolheu a opção:"
def mostrar_escolha():
    escolha = opcao_var.get()
    messagebox.showinfo("Seleção", f"{laranja_texto} {escolha}")

# Janela principal
root = tk.Tk()
root.title("Exemplo de Radiobutton")
root.geometry("300x200")

# Variável que guarda o valor selecionado
opcao_var = tk.StringVar(value="Opção 1")

# Rótulo de instrução
label = tk.Label(root, text="Escolha uma opção:")
label.pack(pady=10)

# Criando os Radiobuttons
r1 = tk.Radiobutton(root, text="Opção 1", variable=opcao_var, value="Opção 1")
r1.pack(anchor="w", padx=50)

r2 = tk.Radiobutton(root, text="Opção 2", variable=opcao_var, value="Opção 2")
r2.pack(anchor="w", padx=50)

# Botão para confirmar a seleção
botao = tk.Button(root, text="Mostrar Escolha", command=mostrar_escolha)
botao.pack(pady=20)

root.mainloop()
