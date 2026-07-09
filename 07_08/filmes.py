# Criar um programa usando funções:
# 1 - Quantidade total de filmes 
# 2 - Informações de um filme pelo título
# 3 - Filmes de um diretor específico
# 4 - Filmes de um gênero específico
# 5 - Média de duração dos filmes
# 6 - Sair

def menu():
    print("0 - Adicionar filme (opcional)")
    print("1 - Quantidade total de filmes") 
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")

while True:
    menu()
    opcao = input("Selecione a opção desejada (0 a 6):").strip()

    if opcao == '0':
        print("adicionar_filme()")
    if opcao == '1':
        print("adiciona_filme()")
    if opcao == '2':
        print("info_por_titulo()")
    if opcao == '3':
        print("filmes_por_diretor()")
