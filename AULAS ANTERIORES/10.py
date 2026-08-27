lista = []

while True:
  numero = int(input("Digite um número (0 para sair): "))

  if numero == 0:
    break
  lista.append(numero)

for numero in lista:
  print(numero)


#Exercício
# Exibir o maior e o menor número da lista


lista = []

while True:
  numero = int(input("Digite um número (0 para sair): "))

  if numero == 0:
    break
  lista.append(numero)

print(f"Menor:",(min(lista)))
print(f"Maior:",(max(lista)))



#Exercício
#Remover duplicados da lista


lista = [1,2,3,2,4,5,2,6,7,8,4]
lista_2 = []

for numero in lista:
  if numero not in lista_2:
    lista_2.append(numero)

print(f"De:", lista)
print(f"Para:", lista_2)


# #Estrutura de Dados - Matriz
# **Matriz** é uma **estrutura de dados bidimensional**, que organiza os dados em forma de **linhas e colunas**, semelhante a uma tabela.


# Criando Matrizes com append
# Ao usar append com uma lista como paramentro, pyhton adicona a lista inteira como um único elemento - não os intens individualmente. Isso é exatamante o que precisamos para construir matrizes linha a linha.


lista = []
lista.append(["a","b"])
lista.append(["c","d"])

print(len(lista))
print(lista)


# Acessando elementos de uma Matriz
# Para acessar um elemento especifico, usamos dois pares de colchetes: o primeiro seleciona a linha, o segundo seleciona a coluna.

lista = [["a","b"],["c","d"]]

print(lista [0])
print(lista[1])
print(lista[0][0])
print(lista[1][0])


# Excercício 1

# Matriz 3x3 Formatada

# Escreva um programa que defina uma matriz 3x3 e a imprima no formato de linhas e colunas, simulando uma tabela.



matriz = [[1,2,3],[4,5,6],[7,8,9]]

print("Matriz 3x3: ")
for linha in matriz:
  print() #somente para a estética
  for coluna in linha:
    print(f"[{coluna}]\t", end="")
  print() #somente para a estética



#Exercicio 2

# **Somando todos os elementos ** Modifique o programa anterior para calcular e exibir a soma de todos os elemntos da matriz 3x3


matriz = [[1,2,3],[4,5,6],[7,8,9]]
soma= 0

print("     Matriz 3x3: ")
for linha in matriz:
  print()
  for coluna in linha:
    print(f"[{coluna}]\t", end="")
    soma += (coluna)
  print()

print()
print(f"A soma é: {soma}")


# Exericio 3

# Buscando um número na matriz 5x5: Escreva um programa que defina uma matriz 5x5, peça um número inteiro ao usuário e informe:

#     Se o número existe na matriz
#     Qual é sua posição [linha, coluna]


matriz = [
    [33,45,22,14,55],
    [52,32,42,25,82],
    [21,50,40,31,20],
    [65,26,77,29,24],
    [33,10,11,48,99]
]

numero = int(input("Digite um número: "))

encontrado = False

for linha in range(5):
  for coluna in range(5):
    if matriz [linha][coluna] == numero:
      print(f"O número {numero} existe na posição {[linha],[coluna]}")
    encontrado = True

if not encontrado:
  print(f"O número {numero} não existe na matriz.")





# Isto está formatado como código

continuação da aula anterior:
[ ]

lista = []

while True:
  numero = int(input("Digite um número (0 para sair): "))

  if numero == 0:
    break
  lista.append(numero)

for numero in lista:
  print(numero)

Digite um número (0 para sair): 4
Digite um número (0 para sair): 5
Digite um número (0 para sair): 6
Digite um número (0 para sair): 1
Digite um número (0 para sair): 5
Digite um número (0 para sair): 2
Digite um número (0 para sair): 0
4
5
6
1
5
2

Exercício

Exibir o maior e o menor número da lista
[ ]

lista = []

while True:
  numero = int(input("Digite um número (0 para sair): "))

  if numero == 0:
    break
  lista.append(numero)

print(f"Menor:",(min(lista)))
print(f"Maior:",(max(lista)))

Digite um número (0 para sair): 4
Digite um número (0 para sair): 5
Digite um número (0 para sair): 6
Digite um número (0 para sair): 1
Digite um número (0 para sair): 0
Menor: 1
Maior: 6

Exercício

Remover duplicados da lista
[ ]

lista = [1,2,3,2,4,5,2,6,7,8,4]
lista_2 = []

for numero in lista:
  if numero not in lista_2:
    lista_2.append(numero)

print(f"De:", lista)
print(f"Para:", lista_2)

De: [1, 2, 3, 2, 4, 5, 2, 6, 7, 8, 4]
Para: [1, 2, 3, 4, 5, 6, 7, 8]

Estrutura de Dados - Matriz

Matriz é uma estrutura de dados bidimensional, que organiza os dados em forma de linhas e colunas, semelhante a uma tabela.
Criando Matrizes com append

Ao usar append com uma lista como paramentro, pyhton adicona a lista inteira como um único elemento - não os intens individualmente. Isso é exatamante o que precisamos para construir matrizes linha a linha.
[ ]

lista = []
lista.append(["a","b"])
lista.append(["c","d"])

print(len(lista))
print(lista)

2
[['a', 'b'], ['c', 'd']]

Acessando elementos de uma Matriz

Para acessar um elemento especifico, usamos dois pares de colchetes: o primeiro seleciona a linha, o segundo seleciona a coluna.
[ ]

lista = [["a","b"],["c","d"]]

print(lista [0])
print(lista[1])
print(lista[0][0])
print(lista[1][0])

['a', 'b']
['c', 'd']
a
c

Excercício 1

Matriz 3x3 Formatada

Escreva um programa que defina uma matriz 3x3 e a imprima no formato de linhas e colunas, simulando uma tabela.
[ ]

matriz = [[1,2,3],[4,5,6],[7,8,9]]

print("Matriz 3x3: ")
for linha in matriz:
  print() #somente para a estética
  for coluna in linha:
    print(f"[{coluna}]\t", end="")
  print() #somente para a estética

Matriz 3x3: 

[1]	[2]	[3]	

[4]	[5]	[6]	

[7]	[8]	[9]	

Exercicio 2

**Somando todos os elementos ** Modifique o programa anterior para calcular e exibir a soma de todos os elemntos da matriz 3x3
[ ]

matriz = [[1,2,3],[4,5,6],[7,8,9]]
soma= 0

print("     Matriz 3x3: ")
for linha in matriz:
  print()
  for coluna in linha:
    print(f"[{coluna}]\t", end="")
    soma += (coluna)
  print()

print()
print(f"A soma é: {soma}")

Matriz 3x3: 

[1]	[2]	[3]	

[4]	[5]	[6]	

[7]	[8]	[9]	

A soma é: 45

Exericio 3

Buscando um número na matriz 5x5: Escreva um programa que defina uma matriz 5x5, peça um número inteiro ao usuário e informe:

    Se o número existe na matriz
    Qual é sua posição [linha, coluna]

[ ]

matriz = [
    [33,45,22,14,55],
    [52,32,42,25,82],
    [21,50,40,31,20],
    [65,26,77,29,24],
    [33,10,11,48,99]
]

numero = int(input("Digite um número: "))

encontrado = False

for linha in range(5):
  for coluna in range(5):
    if matriz [linha][coluna] == numero:
      print(f"O número {numero} existe na posição {[linha],[coluna]}")
    encontrado = True

if not encontrado:
  print(f"O número {numero} não existe na matriz.")



# Exercício 4

# Desenvolva um programa que simule o controle de assentos de um cinema:

# O cinema possui 5 fileiras (linhas) e 10 assentos (colunas)

# Os Assentos devem se r representador por uma matriz (lista de listas):

# -"L" para indicar livre

# -"O" para indicar ocupado

# No ínicio do programa: todos os assentos devem estar livres("L")

# O Programa deve:

# Exibir uma mensagem pedindo ao usuário?

# -O número da linha.

# -O número da coluna.

# Receber esses valores via entrada(input).

# Marcar o assento escolhodo como ocupado (O).

# Mostrar o mapa atualizado dos assentos.


cinema = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append("L")
    cinema.append(linha)

while True:
    print("\n                  MAPA DO CINEMA") #estético
    print("   A","   B", "   C", "   D","   E") #estético
    cont = 1  #usar cont para mostrar o número das linhas
    for i in cinema:
      print(f"{cont}{i}")
      cont = cont+1

    #escolher o assento
    coluna_escolhida = (input("\nDigite a coluna desejada (A, B, C, ou E) ou digite 0 para sair: "))
    linha_escolhida = int (input("\nDigite a linha desejada (1, 2, 3, 4 ou 5): "))

    #usando index para pegar a posição da Letra desejada na coluna
    coluna_index = coluna.index(coluna_escolhida)

    #informar se o assento foi reservado ou ele está ocupado
    if cinema[coluna_index][linha_escolhida-1] == "O":
        print("Assento já ocupado!")

    if cinema[coluna_index][linha_escolhida-1] == "L":
      print(f"Assento {coluna_escolhida}{linha_escolhida} reservado com sucesso!")


         #encerrar programa
    if coluna_escolhida == "0":
      print("Programa encerrado.")
      break




#versão do professor

linhas = 5
colunas = 10

cinema = []
linha = []

for j in range(colunas):
  linha.append("L")

for i in range(colunas):
  cinema.append(linha)


linha_escolhida=int (input("Digite a linha (0 a 4): "))
coluna_escolhida=int(input("Digite a coluna (0 a 9): "))




# jogo da velha com matrizes #exibir tabuleiro #verificar vitória #jogar

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro():
    print("\nTabuleiro:\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("---------")

exibir_tabuleiro()

def verificar_vitoria():
    #verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return True

    #verificar colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] != " ":
            return True

    #verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return True

    return False

def jogar():
    jogador = "X"
    for _ in range(9):
        exibir_tabuleiro()
        linha = int(input(f"Jogador {jogador}, escolha a linha (0-2): "))
        coluna = int(input(f"Jogador {jogador}, escolha a coluna (0-2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            if verificar_vitoria():
                exibir_tabuleiro()
                print(f"Jogador {jogador} venceu!")
                return
            jogador = "O" if jogador == "X" else "X"
        else:
            print("Posição já ocupada. Tente novamente.")



jogar()



# Versão Simplificada e Melhorada do Jogo da Velha

# Esta versão inclui validação para as entradas do jogador (garantindo que as coordenadas estejam dentro do tabuleiro e que a casa escolhida não esteja ocupada) e também uma verificação para condição de empate.


tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro():
    print("\nTabuleiro:\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("---------")

def verificar_vitoria():
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return True

    # Verificar colunas
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] != " ":
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return True

    return False

def jogar():
    jogador = "X"
    movimentos = 0
    while True:
        exibir_tabuleiro()

        while True:
            try:
                linha = int(input(f"Jogador {jogador}, escolha a linha (0-2): "))
                coluna = int(input(f"Jogador {jogador}, escolha a coluna (0-2): "))

                if not (0 <= linha <= 2 and 0 <= coluna <= 2):
                    print("Coordenadas inválidas. Por favor, escolha linhas e colunas entre 0 e 2.")
                elif tabuleiro[linha][coluna] != " ":
                    print("Posição já ocupada. Tente novamente.")
                else:
                    break # Saia do loop de entrada se as coordenadas forem válidas
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        tabuleiro[linha][coluna] = jogador
        movimentos += 1

        if verificar_vitoria():
            exibir_tabuleiro()
            print(f"Jogador {jogador} venceu!")
            return

        if movimentos == 9: # Todos os 9 movimentos foram feitos e ninguém venceu
            exibir_tabuleiro()
            print("Empate!")
            return

        jogador = "O" if jogador == "X" else "X"

jogar()




