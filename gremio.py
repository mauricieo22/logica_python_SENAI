from tkinter import Tk,Canvas

janela = Tk()
janela. geometry("500x400")

canvas = Canvas(janela, width= 400, height= 300, bg="black")

canvas.create_oval(30,30,250,250, fill= "blue", outline= "white")
canvas.create_oval(35,60,210,210, fill= "white", outline= "black")


canvas.pack()
janela.mainloop()