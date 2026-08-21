valor_1 = input("Digite um Valor: ")
valor_2 = input("Digite um Valor: ")

valor_3 = input("Digite 1 = mais \n e 2 = menos: ")

if valor_3 == "1":
  soma = int(valor_1)+int(valor_2)
  print(soma)

if valor_3 == "2":
  subtracao = int(valor_1)-int(valor_2)
  print(subtracao)