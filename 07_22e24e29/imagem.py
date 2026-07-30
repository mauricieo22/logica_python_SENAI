from tkinter import Tk, Label, PhotoImage

# Cria a janela principal
root = Tk()
root.title("Exibir PNG no Tkinter")
root.geometry("600x600")

# Carrega a imagem PNG usando a classe nativa PhotoImage
# Nota: Certifique-se de que o arquivo 'imagem.png' está na mesma pasta
imagem_png = PhotoImage(file="Imagem.png")

# Cria um rótulo (Label) para conter e exibir a imagem
rotulo = Label(root, image=imagem_png)
rotulo.pack(expand=True)

# Mantém a referência da imagem para evitar que o coletor de lixo a apague
rotulo.imagem = imagem_png

# Inicia o loop da aplicação
root.mainloop()