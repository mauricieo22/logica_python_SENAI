# #**Estruturas de dados**


# #**FILAS** - coceito, aplicações e implementações em Python.



# Comandos para adicionar e remover elementos de uma lista:
# - append() - adiciona no final da lista
# - pop(0) - remove do inicio da lista

# A combinação desses dois métodos garante o comportamento FIFO usando apenas uma lista padrão.



fila = []

if not fila: #verifica se a fila está vazia ou não
 print("Fila vazia")



# PILHAS no Dia a Dia


# Toda Pilha oferece quatro operações fundamentais.

#     Push (inserir)

#     Pop (remover)

#     Peek/Top (consultar topo)

#     IsEmpty (verificar se está vazia)


# Exemplo prático: inverter uma String


texto = "PYTHON"
pilha = []

#Empilha cada caractere
for char in texto:
  pilha.append(char)

resultado = ""
#Desempilha na ordem inversa
while pilha:
  resultado += pilha.pop()

print(resultado)


# Exercicio 1

# Fila Simples

# Crie um programa que:

#     crie uma fila vazia.

#     Adicione 3 nomes informados pelo usuário.

#     Remova o primeiro nome da fila

#     mostre a fila atual

# objetivo: praticar append() e pop(0)


fila = []

for i in range(3):
  nome = input("Insira um nome:")
  fila.append(nome)

if fila:
  removido = fila.pop(0)
  print(f"\nRemovido: {removido}")
else:
  print("Fila vazia!")

print(f"Fila atual: {fila}")



# Exercicio 2:

# Controle de atendimento

# Simule uma fila de atendimento:

# -Permita inserir pessoas na fila

# -Permita chamar a próxima pessoa.

# -Mostre mensagens como:

#     "Fila vazia!"
#     "Atendendo: João"



#criando fila vazia:
fila = []

#adicionando um menu de opções
while True: #para o programa rodar até o usuário encerrar
  print("\n1 - Adicionar pessoa") #adicionar nome a fila
  print("\n2 - Atender pessoa")   #verificar atendimento
  print("\n3 - Sair")             #encerrar programa

  opcao = input("\nEscolha: ")

  #inserir pessoas na fila:
  if opcao == "1":
    nome = input("Nome: ")
    fila.append(nome)

  #verificar quem está sendo atendido:
  elif opcao == "2":
    if not fila:
      print("Fila vazia!")
    else:
      print(f"Atendendo: {fila.pop(0)}")

  #encerrar o programa:
  elif opcao == "3":
    print("\nAtendimento encerrado!")
    break

  #caso digitado algo além das 3 opções:
  else:
    print("\nOpção inválida!")




# Exercício 3

# Pilha Simples

# Crie um programa que:

#     Crie uma pilha vazia

#     Empilhe 5 números

#     Desempilhe 2 números da pilha

#     Mostre o estado final da pilha



pilha = []

#Pedindo 5 números na pilha:
for i in range(5):
  numero = input("Insira um numero: ")
  pilha.append(numero)

#removendo 2 números:
for i in range (2):
  if pilha:
    removido = pilha.pop()
    print(f"\nRemovido: {removido}")
  else:
    print("\nPilha vazia!")

#mostrando a pilha atualizada:
print(f"\nPilha atual: {pilha}")



# Exercício 4

# Verificar palíndromo

# Crie um programa que:

#     Leia uma palavra

#     Use pilha para verificar se é palíndromo

# Exemplos:

# arara = é palíndromo

# python = não é



pilha = []
palavra = input("Insira a palavra: ")

#separando as letras das palavras para criar uma pilha:
for char in palavra:
  pilha.append(char)

#desempilhando na ordem inversa
invertida = ""
while pilha:
  invertida += pilha.pop()

#verificando se é palíndromo ou não:
if invertida == palavra:
  print("É palindromo!")
else:
  print("NÃO é palindromo!")



# Exercício 6
# Sistema de atendimento

# Desenvolver um sistema que utilize:

#     Fila - Controle de atendimento (FIFO)

#     Pilha - histórico de atendimentos (LIFO)

#     Dicionário - armazenamento de dados do cliente

# Crie um programa em pyhton com o seguinte menu:

# 1- Adicionar Cliente

# 2- Atender cliente

# 3- Mostrar fila

# 4- Mostrar histórico (pilha)

# 5- Buscar cliente

# 6- Sair
# 1. Adicionar cliente

# -Solicitar: Nome e idade

# -Armazenar em um dicionário

# -Inserir o cliente na fila

# Exemplo de estrutura: cliente = {"Nome": "Ana", "Idade": "25")
# 2. Atender cliente

# -Remover da fila(FIFO)

# -Mostrar o cliente atendido

# -Salvar na pilha (histórico)
# 3. Mostrar fila

# -Exibir todos os clientes na ordem de atendimento.
# 4. Mostrar histórico

# -Mostrar os clientes já atendidos

# -Ordem: último atendido primeiro (LIFO)

# 5.Buscar cliente

# -Solicitar nome

# -Verificar:

# se está na fila

# se já foi atendido
# 6. Tratamentos obrigatórios

# -Não permitir remover de fila vazia

# -Não permitir buscar com lista vazia

# -Mensagens claras ao usuário.

fila = []
historico = []

while True:
    print("\n______Menu______")
    print("\n1 - Adicionar Cliente")
    print("2 - Atender Cliente")
    print("3 - Mostrar Fila")
    print("4 - Mostrar Histórico")
    print("5 - Buscar Cliente")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        idade = input("Idade do cliente: ")
        cliente = {"Nome": nome, "Idade": idade}
        fila.append(cliente)
        print(f"Cliente {nome} adicionado à fila.")

    elif opcao == "2":
        if not fila:
            print("Fila vazia! Nenhum cliente para atender.")
        else:
            cliente_atendido = fila.pop(0)
            historico.append(cliente_atendido)
            print(f"Atendendo: {cliente_atendido['Nome']} (Idade: {cliente_atendido['Idade']})")

    elif opcao == "3":
        if not fila:
            print("Fila vazia!")
        else:
            print("\n--- Fila de Atendimento ---")
            for i, cliente in enumerate(fila):
                print(f"{i+1}. Nome: {cliente['Nome']}, Idade: {cliente['Idade']}")

    elif opcao == "4":
        if not historico:
            print("Histórico de atendimentos vazio!")
        else:
            print("\n--- Histórico de Atendimentos (Último atendido primeiro) ---")
            # Imprime o histórico na ordem LIFO (do último adicionado para o primeiro)
            for i, cliente in enumerate(reversed(historico)):
                print(f"{i+1}. Nome: {cliente['Nome']}, Idade: {cliente['Idade']}")

    elif opcao == "5":
        nome_busca = input("Digite o nome do cliente para buscar: ")
        encontrado = False

        # Buscar na fila
        for cliente in fila:
            if cliente['Nome'].lower() == nome_busca.lower():
                print(f"Cliente '{nome_busca}' está na fila de atendimento. Idade: {cliente['Idade']}.")
                encontrado = True
                break

        # Buscar no histórico se não encontrado na fila
        if not encontrado:
            for cliente in historico:
                if cliente['Nome'].lower() == nome_busca.lower():
                    print(f"Cliente '{nome_busca}' já foi atendido. Idade: {cliente['Idade']}.")
                    encontrado = True
                    break

        if not encontrado:
            print(f"Cliente '{nome_busca}' não encontrado na fila nem no histórico.")

    elif opcao == "6":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida! Por favor, escolha uma opção de 1 a 6.")