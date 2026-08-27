from tkinter import Tk,Canvas

janela = Tk()
janela. geometry("500x400")

canvas = Canvas(janela, width= 400, height= 300, bg="skyblue")

canvas.create_oval(80,80,150,150, fill= "pink", outline= "white")
canvas.create_oval(200,200,400,250, fill= "green", outline= "white")

canvas.pack()
janela.mainloop()