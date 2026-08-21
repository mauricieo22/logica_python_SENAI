# #Exercício 1
# **Cadastro de alunos e notas:**
# Crie um programa que:

# -Crie um dicionário com **nome do aluno como chave** e **nota como valor**

# -Permita cadastrar 3 alunos

# -Mostre todos os alunos e suas notas


alunos = {} #dicionário

for i in range (3):                               #pede as informações 3 vezes
  nome = input("Digite o nome do aluno: ")        #pede o nome do aluno
  nota = float(input("Digite a nota do aluno: ")) #pede a nota do aluno
  alunos[nome] = nota                             #inclui nome e nota no dicionário

#exibir um abaixo do outro
for nome,nota in alunos.items():
    print(f"Aluno: {nome} - Nota: {nota}")



#somar as notas e mostra a média

alunos = {} #dicionário

for i in range (3):                               #pede as informações 3 vezes
  nome = input("Digite o nome do aluno: ")        #pede o nome do aluno
  nota = float(input("Digite a nota do aluno: ")) #pede a nota do aluno
  alunos[nome] = nota                             #inclui nome e nota no dicionário

soma = 0

#exibir um abaixo do outro

for nome,nota in alunos.items():
  print(f"\nAluno: {nome} \nNota:  {nota}")
  soma = soma+nota

media = soma / len(alunos)

print(f"\nA média das notas é: {media:.1f}") #Calcula e mostra a média



# Exercício 2:

# Pedir um produto ao usuário, se ele existir no dicionário exiba o valor, se não existir mostrar a mensagem de produto não existente.



tabela = {
    "Alface": 1.99,
    "Batata": 4.99,
    "Áçucar": 6.99,
    "Carne" : 45.99
}
while True:
  produto = input("\nDigite o nome do Produto: ")

  if produto in tabela:
   print(f"O valor do produto é: {tabela[produto]:.2f}")
  else:
    print("PRODUTO NÃO ENCONTRADO")



# Exerício 3:

# Crie um programa que:

# -Peça uma frase(com palavras repetidas)




dicionario = {} #criando um
contador = 0


frase = input("Digite uma frase: ")

#separa as palavras da frase
lista_palavras = frase.split()

for palavra in lista_palavras:
  if palavra not in dicionario:
    dicionario[palavra] = 1
  else:
    dicionario[palavra] = dicionario[palavra]+1
for palavra, quant in dicionario.items():
  print(f"{palavra}: {quant}")

print(len(dicionario))