import tkinter as tk
root = tk.Tk()

img = tk.PhotoImage(file="icone.png")

label = tk.Label(root, image=minha_imagem)
label.image = img
label.pack(expand=True)

root.mainloop()