#break


soma = 0

while True:
  valor = int(input("Digite um número (0 para sair): "))
  if valor == 0:
    break
  soma += valor
print(f"Soma: {soma}")



#Exercício: Tabuada


num = int(input("Digite o número: "))
x = 1

while x <= 10:
    resultado = num * x
    print(f"{num} x {x} = {resultado}")
    x += 1



#Repetições Aninhadas

t = 1
while t <= 10:
  n = 1
  print(f"Tabuada de {t}")
  print(f"="*15)
  while n <= 10:
    print(f"{t} x {n} = {t * n}")
    n += 1
  t += 1



#Exercício: pedir a tabuada em looping e adicionar uma parada

while True:
  valor = int(input("Digite um número (0 para sair): "))
  if valor == 0:
    break
  n = 1
  print(f"A tabuada do {valor} é:")
  print()
  while n <= 10:
    print(f"{valor} x {n} = {valor * n}")
    n += 1
    print()



t = 1
while t <= 10:
  t = int(input("De qual número deseja calcular a tabuada? "))
  if t >= 11:
    print("Programa Finalizado")
    break
  n = 1
  print(f"Tabuada de {t}: ")
  print(f"="*15)

  while n <= 10:
    print(f"{t} x {n} = {t * n}")
    n += 1



t = 1
while t <= 10:
  t = int(input("De qual número deseja calcular a tabuada? "))
  if t >= 11:
    print("Programa Finalizado")
    break

  oper = input( "Digite a operação (+, -, *, /): ")
  n = 1
  print(f"Tabuada de {t}: ")
  print(f"="*15)
  while n <= 10:
    if(oper == "+"):
      print(f"{t} + {n} = {t + n}")
    elif(oper == "-"):
      print(f"{t} - {n} = {t - n}")
    elif(oper == "*"):
      print(f"{t} * {n} = {t * n}")
    elif(oper == "/"):
      print(f"{t} / {n} = {t / n}")
    else:
      print("Operação inválida")
      break

      n += 1



