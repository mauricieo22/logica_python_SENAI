#if, else

idade = 18

if idade >= 18:
  print("Maior de idade")



idade = 18

if idade >= 18:
  print("Maior de idade")

else:
  print("Menor de idade")



idade = 14

if idade >= 18:
  print(f"Maior de idade.")
  print(f"Sua idade é {idade-18} anos maior que 18.")

else:
  print(f"Menor de idade.")
  print(f"Sua idade é {18-idade} anos menor que 18.")



#elif:

nota = 9

if nota >= 7:
  print("Aprovado")

elif nota >= 5:
  print("Em recuperação")

else:
  print("Reprovado")



nota = 4

if nota > 9:
  print("conceito A")

elif nota > 7:
  print("conceito B")

elif nota >= 6:
  print("conceito C")

elif nota >= 5:
  print("conceito D")

else:
  print("conceito E")



#verificar número par ou ímpar

numero = 4
if numero % 2 == 0:
  print("Número par")

else:
  print("Número ímpar")



#verificar número par ou ímpar

numero = 4
if numero % 2 == 0:
  print("Número par")

else:
  print("Número ímpar")



#verificar número par ou ímpar

numero = 4
if numero % 2 == 0:
  print("Número par")

else:
  print("Número ímpar")



#Exercícios:

numero = int(input("Digite o número:"))

if numero > 0:
  print("Seu número é positivo.")

elif numero == 0:
  print("Seu número é: 0")

else:
  print("Seu número é negativo.")



nota_1 = int(input("Digite 1ª nota: "))
nota_2 = int(input("Digite 2ª nota: "))
nota_3 = int(input("Digite 3ª nota: "))

media = (nota_1+nota_2+nota_3) /3

if media > 7:
  print("Aprovado")

elif media >= 5:
  print("Recuperação")

else:
  print("Reprovado")



idade = int(input("Digite a idade: "))

if idade > 18:
  print("Adulto")

elif idade > 12:
  print("Adolescente")

else:
  print("Criança")



#if  - and,or


nota = 9
faltas = 8

if(nota>=7) and (faltas <= 5):
  print("Aprovado")
else:
  print("Reprovado")



nota = 9
faltas = 8

if(nota>=7) and (faltas <= 5):
  print("Aprovado")
else:
  print("Reprovado")