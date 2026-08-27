from tkinter import Tk,Canvas

janela = Tk()
janela. geometry("500x400")

canvas = Canvas(janela, width= 400, height= 300, bg="skyblue")

canvas.create_rectangle(
    50, 50, 200, 150,
    fill= "black",
    outline= "red"
)

canvas.pack()
janela.mainloop()