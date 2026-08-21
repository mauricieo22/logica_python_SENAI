# Nesta aula estamos aprendendo a:

# Dobrar um número com código;
# Converter um valor;
# Calcular a área de um triângulo;
# Calcular o troco;
# Calcular média ponderada.

# f = código com texto e variáveis que estão entre chaves {}
# facilita para por o código em uma string só.
# usar int para números inteiros e float para números com decímais.

#como dobrar um número:

valor_1 = int (input("informe o número a ser dobrado: "))
valor_2 = int (2)

dobro = (valor_1) * 2

print(f"o número informado foi: {valor_1}, seu dobro é: {dobro}")

#como converter um número:

#minha versão


valor_1 = float (input("Digite a temperatura em Celsius: "))

conversão = (valor_1) *9/5+32

print(f"a temperatura em Celsius informada foi: {valor_1}, corresponde a: {conversão} Fahrenheit")



#versão do professor


celcius = float(input("informe a temperatura em ºC: "))

fahrenheit = (celcius * 9/5) + 32

print(f"a temperatura de {celcius:.1f}ºC corresponde a {fahrenheit:.1f}ºF")

#calcular a área de um Triângulo

#minha versão


base = float (input("Digite a base:" ))

altura = float (input("Digite a altura:" ))

print(f"A área do triângulo é: {base*altura/2} ")

#calcular a área de um Triângulo

#minha versão


base = float (input("Digite a base:" ))

altura = float (input("Digite a altura:" ))

print(f"A área do triângulo é: {base*altura/2} ")

from re import M
#calcule média ponderada

nota_1 = float (input("Digite a nota da prova 1: "))

nota_2 = float (input("Digite a nota da prova 2: "))

nota_3 = float (input("Digite a nota da prova 3: "))

media = (nota_1*2+nota_2*3+nota_3*5) /10

print(f"a média final é: {media:.1f}")