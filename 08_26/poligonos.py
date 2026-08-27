from tkinter import Tk,Canvas

janela = Tk()
janela. geometry("500x400")

canvas = Canvas(janela, width= 400, height= 300, bg="yellow")

canvas.create_polygon(60,50,10,100,35,150,85,150,110,100, fill= "orange", outline= "black")

canvas.pack()
janela.mainloop()