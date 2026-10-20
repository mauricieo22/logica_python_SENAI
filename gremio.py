import customtkinter as ctk

# Configuração do tema (opcional)
ctk.set_appearance_mode("System")  # Opções: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Opções: "blue", "green", "dark-blue"

# Criando a janela principal
janela = ctk.CTk()
janela.title("Meu App com CustomTkinter")
janela.geometry("400x300")

# Função que será executada ao clicar no botão
def clique_botao():
    print("O botão foi clicado!")

# Criando um texto (Label)
texto = ctk.CTkLabel(janela, text="Olá, CustomTkinter!", font=("Arial", 20))
texto.pack(pady=20)

# Criando um botão
botao = ctk.CTkButton(janela, text="Clique Aqui", command=clique_botao)
botao.pack(pady=10)

# Iniciando o loop do aplicativo
janela.mainloop()


