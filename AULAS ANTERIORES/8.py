#Estruturas de repetição: FOR


nome = "Maurício Câmara"

for letra in nome:
  print(letra)


#A Função range () - Básico


#a função range () gera um sequência de nueros inteiros, muito usada com o laço for:

range(fim)
#gera números de 0 até fim - 1

range(inicio,fim)
#gera números de inicio até fim - 1

range(inicio, fim, passo)
#avança com o intervalo definido po passo


for i in range (5):
  print(i)


for i in range (3,8):
  print(i)


#passo positivo
for i in range (0,10,2): #(início, fim e passo)
  print(i)


#contagem regressiva
for i in range (5,0,-1):
  print(i)


# Exercicio 1 - Contando Vogais

# Escreva um programa que peça um texto ao usuário e conte quantas vogais estão presente.


frase = input("Escreva uma frase: ")
vogais = "ÁáAaÃãâÂEeÉéIiÍíOoUuéÉ"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"A frase contém {contador} vogais.")



frase = input("Escreva uma frase: ").lower() #para transformar o texto digitado em minúsculo
vogais = "aeiou"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"A frase contém {contador} vogais.")



# Exercício 2: Vogais e consoantes

# amplie o programa anterior para contar também as consoantes. ignore epaços e cacteries especiais.


frase = input("Escreva uma frase: ")
vogais = "ÁáAaÃãâÂEeÉéIiÍíOoUuéÉ"
consoantes = "BbÇçCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvXxZz"
contador_1 = 0
contador_2 = 0

for letra in frase:
    if letra in vogais:
        contador_1 += 1

    elif letra in consoantes:
      contador_2 += 1

print(f"A frase contém {contador_1} vogais e {contador_2} consoantes.")


frase = input("Escreva uma frase: ")
vogais = "ÁáAaÃãâÂEeÉéIiÍíOoUuéÉ"
consoantes = "BbÇçCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvXxZz"
contador_1 = 0
contador_2 = 0

for letra in frase:
    if letra in vogais:
        contador_1 += 1

    elif letra.isalpha():
      contador_2 += 1

print(f"A frase contém {contador_1} vogais e {contador_2} consoantes.")


# Exercicio 3: Maior número
# escreva um programa que peça para o usuário informar 5 números
# o programa deve exibir o maior valor digitado.


maior_numero = int(input("Digite o 1º número: "))

for i in range (4):
  numero = int(input(f"Digite o {i+2}º número: "))
  if numero > maior_numero:
    maior_numero = numero

print(f"O maior número digitado foi: {maior_numero}")



#versão do professor:

maior = None
for i in range(5):
  num = int (input("Digite um número: "))

  if maior is None or num > maior:
    maior = num
print("Maior número:", maior)