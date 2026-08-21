# Estruturas de Dados

# Uma introdução prática a vetores e listas - os blocos fundamentais para organizar e manipular informações em programas.


lista=[] #lista vazia
lista=[15,8,9] #lista com 3 elementos

print(lista[0]) #15
print(lista[1]) #8
print(lista[2]) #9

#print(lista[5]) #retorna erro pois ultrapassa o número de posições indicadas


lista=[] #lista vazia
lista=[15,8,9] #lista com 3 elementos

print(lista)



lista=[]
lista=[15,8,9]

print(len(lista)) #retorna a quatidade de posições da lista



lista=[]
lista=[15,8,9]

print(len(lista)) #retorna a quatidade de posições da lista



# #ACRESCENTANDO ELEMENTOS
# Para incluir um elemento, no final da lista, utilizamos a função append.



lista = [7,8,9]
print(lista) # [7,8,9]

lista.append(10)
print(lista)      #[7,8,9,10]


# #Exemplo Prático - Média Aritmética
# Calculando a média de notas - Em vez de criar cinco variáveis, usamos uma única para armazenar todas as notas.


notas = [7.5, 8.0, 6.5, 9.0, 8.5]
soma = 0
x = 0

while x < len(notas): #usar len(notas) ao invés de por 5 que é a quantidade total de itens na lista (notas).
    soma += notas[x]
    x += 1  #serve para somar até o último valor da lista

print("A média das notas é:", soma / len(notas))

# x é usado como indice e variável



# #Recebendo dados do usuário
# Uma variação do exemplo anterior, onde as notas são lidas dinamicamente via input():



notas = []
soma = 0
x = 0

while x < 5:
  notain = int(input("Digite a primeira nota: "))
  notas.append(notain)
  x += 1

soma = sum(notas)

print("A média das notas é:", soma / 5)



#Cópias de listas

# Fatiamento de listas (Slicing)

# Use [ínicio:fim] para extrair partes de uma lista. O índice fim é exclusivo. Significa que a sua posição não fará parte da nova lista.


lista = [1,2,3,4,5]

copia = lista [0:5]  #[1,2,3,4,5]
copia = lista [:5]   #[1,2,3,4,5]
copia = lista [1:3]  #[2,3]
copia = lista [1:4]  #[2,3,4]
copia = lista [3:]   #[4,5]
copia = lista [:3]   #[1,2,3]



# #Índices Negativos
# Índices negativos acessam elementos a partir do final da lista. -1 é o último elemento, -2 o penúltimo, e assim por diante.


lista = [1,2,3,4,5]

lista[:-1] #[1,2,3,4]
lista[-1]  #5
lista[-2]  #4



lista = [10,20,30,40]

for i in range (len(lista)):
  print(lista[i])



# removendo elementos com del

lista = ["a","b","c"]

del lista [1]
print(lista) #["a","c"]

del lista [0]
print (lista) # ["c"]


# removendo fatias inteiras com slicing


lista = ["a","b","c","d","e","f"]
del lista [1:5]
print(lista)  #["a","f"]



# Leitura de números até Zero
# Escreva um programa que leia números inteiros do usuário até que 0 seja digitado. Cada número deve ser adicionado a uma lista. Ao final, imprima o conteúdo completo da lista.


lista = []

while True:
  numero = int(input("Digite um número (0 para sair): "))

  if numero == 0:
    break
  lista.append(numero)

print ("Lista completa: ", lista )

