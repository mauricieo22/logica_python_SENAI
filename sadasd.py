from tkinter import Tk, Label, Entry, Button, PhotoImage

root = tk.Tk()
root.title("Senai - Desinvolvimento de Sistemas")   #título da janela
root.geometry("500x300")  

imagem_login = PhotoImage(file="images.png")
label_imagem = Tkinter.Label(root, image=imagem_login, bg="white", width=200, height=200)
label_imagem.pack(side="left")

# Rótulo e Campo de Texto na primeira linha
Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
Entry(root).grid(row=0, column=1, padx=10, pady=10)

# Botão ocupando duas colunas na linha abaixo
Button(root, text="Salvar").grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
