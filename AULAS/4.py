# # Operadores aritméticos

# # Adição Realiza a soma de ambos operandos.

# # Subtração Realiza a subtração de ambos operandos.

# # Multiplicação Realiza a multiplicação de ambos operandos.

# # / Divisão Realiza a Divisão de ambos operandos.

# # // Divisão inteira Realiza a divisão entre operandos e a parte decimal de ambos operandos.

# # % Módulo Retorna o resto da divisão de ambos operandos.

# # ** Exponenciação Retorna o resultado da elevação da potência pelo outro.


# Grupos de procdência

# 1º Parenteses()

# 2º Exponenciação **

# 3º Multiplicação, Divisão, Módulo q

# 4º Adição e subtração


# Operadores relacionais

# == Igual a - Verifica se um valor é igual ao outro != Diferente de - Verifica se um valor é diferente ao outro

#     Maior que - Verifica se um valor é maior que outro = Maior ou igual - Verifica se um valor é maior ou igual ao outro < Menor que - Verifica se um valor é menor que outro <= Menor ou igual - Verifica se um valor é menor ou igual ao outro


# operadores lógicos

# and : Retorna true se ambas as condições forem verdadeiras.

# or : Retorna true se pelo menos uma das condições for verdadeira

# not : Inverte o resultado, retorna False se o resultado for verdadeiro.

# Tabelas Verdade

# AND: True and True = True

# True and False = False

# False and False = False

# OR:

# True or True =True

# True or False =True

# False or True =True

# False or False =False

# NOT:

# not True =False

# not False =True

idade = int(input("qual sua idade? "))
type(idade)



#exemplo 1 : verificar idade para dirigir

idade = 18

habilitação = True

pode_dirigir = idade>= 18 and habilitação

print(f"Pode dirigir: {pode_dirigir}")



#exemplo 2 : sistema de login

usario_correto = "admin"

senha_correta = "1234"

tentativa_usuario = "admin"

tentativa_senha = "5678"


acesso_permitido = (tentativa_usuario == usario_correto) and (tentativa_senha == senha_correta)

print (f"Acesso permitido: {acesso_permitido}")



# exemplo 3 : operador OR

tem_dinheiro = False
tem_credito = True

pode_comprar = tem_dinheiro or tem_credito
print(f"Pode comprar: {pode_comprar}")



# Exemplo 4 : operador NOT

chuva = True

print(f"Está chovendo: {chuva}")
print(f"Está chovendo: {not chuva}")


#precedencia dos operadores lógicos

#exemplos com precedencia

a = True

b = False

c = True



nome = input("Digite seu nome: ")

idade = input("Digite sua idade: ")

altura = input("Digite sua altura: ")



valor_1 = float (input("digite o primeiro valor: "))
valor_2 = float (input("digite o segundo valor: "))

soma = (valor_1+valor_2)

print(f"O resultado é: {soma}")



x = int (input("digite o primeiro valor: "))
y = int (input("digite o segundo valor: "))

soma = x+y

print(soma)



valor_produto = float (input("Valor do produto: " "R$"))

quantidade_produto = float (input("Quantidade de produtos: " ))

print(f"O total é: R${valor_produto*quantidade_produto}")



