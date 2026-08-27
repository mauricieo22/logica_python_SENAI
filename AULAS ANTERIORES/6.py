#Estruturas de repetição
#while


x = 1
while x <= 10:
  print(x)
  x = x + 1


x = 90
while x <= 100:
  print(x)
  x = x + 1


#Exercício: Contagem regressiva

x = 10

while x >= 1 :
  print(x)
  x = x - 1

print("Fogo!")



#Exercício: Contar de 0 a 10 e exibir somente números pares

x = 0

while x <= 10:
  print(x)
  x = x + 2



#Exercício: Contar de 0 a 10 e exibir somente números ímpares

x = 1

while x <= 10:
  print(x)
  x = x + 2



#Exercício: Contar de 0 a 20 e exibir par ao lado dos pares e ímpar ao lado dos impares

x = 0

while x <= 10:

  if x % 2 == 0:
    print(f"{x} par")
  else:
    print(f"{x} impar")

  x = x + 1



#Contadores: Variáveis que Contam


n = int(input("Digite um número: "))
x = 1

while x <= n:
  print(x)
  x = x + 1


n = int(input("Digite um número: "))
x = 1

while x <= n:
  print(x)
  x = x + 1


#Contadores com condições: Corrigindo um teste

pontos = 0

questao = 1

while questao <= 3:
   resposta = input(f"Resposta da questão {questao} (A/B/C/D): ")

   if questao == 1 and resposta == "B":
      pontos = pontos + 1              #acumulador

   if questao == 2 and resposta == "A":
    pontos = pontos + 1

   if questao == 3 and resposta == "D":
     pontos = pontos + 1
   questao = questao + 1

print(f"O aluno fez {pontos} pontos(s)")



# Interrompendo a Repetição com Break

soma = 0

while True:
  valor = int(input("Digite um número (0 para sair): "))
  if valor == 0:
    break

  soma += valor

print (f"Soma = {soma}")
