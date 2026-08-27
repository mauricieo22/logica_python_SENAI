from tkinter import Tk,Canvas

janela = Tk()
janela. geometry("500x400")

canvas = Canvas(janela, width= 400, height= 300, bg="orange")

canvas.create_line(10, 250, 250, 250, fill="white", width= 3)
canvas.create_line(10, 10, 10, 250, fill="black", width= 3)
canvas.create_line(10, 10, 250, 250, fill="blue", width= 3)
canvas.create_line(10, 10, 250, 10, fill="green", width= 3)
canvas.create_line(10, 250, 250, 10, fill="purple", width= 3)


canvas.pack()
janela.mainloop()