from tkinter import Tk,Canvas

janela = Tk()
janela. geometry("600x310")

canvas = Canvas(janela, width= 860, height= 300, bg="skyblue")


#grama
canvas.create_rectangle(0,305,600,290, fill= "green", outline= "green")
#parede
canvas.create_rectangle(330, 300, 70, 150, fill= "#f5f5dc")
#telhado
canvas.create_polygon(60,155,200,40,340,155, fill="#8b3e2f")
#porta
canvas.create_rectangle(230, 300, 170, 200, fill= "#8b3e2f")
#janela 1
canvas.create_rectangle(150, 250, 90, 200, fill= "white")
#janela 2
canvas.create_rectangle(250, 250, 310, 200, fill= "white")
#linha horizontal janela 1 
canvas.create_line(90, 225, 150, 225, fill="black", width= 2)
#linha vertical janela 1 
canvas.create_line(120, 250, 120, 200, fill="black", width= 2)
#linha horizontal janela 2 
canvas.create_line(250, 225, 310, 225, fill="black", width= 2)
#linha vertical janela 2 
canvas.create_line(280, 250, 280, 200, fill="black", width= 2)
#maçaneta
canvas.create_oval(175,250,180,240, fill= "#eeb422", outline= "#eeb422")

#sol
canvas.create_oval(-10,-10,70,70, fill= "yellow", outline= "white")
#nuvens
canvas.create_oval(280,-10,370,20, fill= "white", outline= "white")
canvas.create_oval(290,15,340,35, fill= "white", outline= "white")
canvas.create_oval(295,20,320,45, fill= "white", outline= "white")
canvas.create_oval(270,30,310,80, fill= "white", outline= "white")
#chaminé
canvas.create_rectangle(265,70,310,150, fill= "#8b3e2f", outline= "#8b3e2f")
#flor (caule)
canvas.create_line(35, 300, 35, 275, fill="green", width= 2)
#flor petalas
canvas.create_oval(30, 275, 40, 265, fill="yellow", outline="yellow")
canvas.create_oval(25, 266, 35, 257, fill="#eec900", outline="#eec900")

#carro carroceria
canvas.create_polygon(350,290,350,370, 270,50, 420,250,420,290, fill= "gray", outline= "black")





canvas.pack()
janela.mainloop()