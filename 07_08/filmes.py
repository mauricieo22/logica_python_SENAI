# Criar um programa usando funções:
# 1 - Quantidade total de filmes 
# 2 - Informações de um filme pelo título
# 3 - Filmes de um diretor específico
# 4 - Filmes de um gênero específico
# 5 - Média de duração dos filmes
# 6 - Sair


def menu():
    print("Selecione a opção desejada (0 a 6):")   
    print("0 - Adicionar filme (opcional)")
    print("1 - Quantidade total de filmes") 
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")


#opção 1:
def quantidade_total_de_filmes():
    contador = 0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            for linha in f:
                if linha.strip().startswith("Título:"):
                    contador += 1
    except FileNotFoundError:
        print("Arquivo'filmes.txt' não encontrado.")
        return 0
    print(f"\nQuantidade total de filmes: {contador}\n")
    return contador


#opção 2:
def info_por_titulo():
    titulo_busca = input("Digite o título do filme: ").strip().lower()
    encontrado = False
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            for linha in f:
                if linha.strip().lower().startswith(f"Título:"):
                    titulo = linha.split(":",1) [1] .strip()
                    if titulo.lower() == titulo_busca:
                        print(f"Título:{titulo}")
                        try:
                            ano = next(f).strip()
                            diretor = next(f).strip()
                            genero = next(f).strip()
                            duracao = next(f).strip()                        
    except StopIteration:
        print("Registro incompleto para esse título."
        return
        print(ano)
        print(diretor)
        print(genero)
        print(duracao)
        encontrado = True
        break            


#opção 3:
def filmes_por_diretor():
    diretor = input("Digite o nome do diretor: ")
    with open("filmes.txt", "r") as f:
        filmes = f.readlines()
    for filme in filmes:
        if diretor in filme:
            print(filme.strip())


#opção 4:
def filmes_por_genero():
    genero = input("Digite o gênero do filme: ")
    with open("filmes.txt", "r") as f:
        filmes = f.readlines()
    for filme in filmes:
        if genero in filme:
            print(filme.strip())


#opção 5:
def media_duracao():
    with open("filmes.txt", "r") as f:
        filmes = f.readlines()
    total_duracao = 0
    for filme in filmes:
        duracao = int(filme.strip().split(",")[3])
        total_duracao += duracao
    media = total_duracao / len(filmes) if filmes else 0
    print(f"Média de duração dos filmes: {media:.2f} minutos")


#bloco principal de execução (último)
if __name__ == "__main__":
    while True:
        menu()
        opcao = input("Selecione a opção desejada (0 a 6):").strip()

        if opcao == '0':
            adicionar_filme()
        if opcao == '1':
            quantidade_total_de_filmes()
        elif opcao == '2':
            info_por_titulo()
        elif opcao == '3':
            filmes_por_diretor()
        elif opcao == '4':
            filmes_por_genero()
        elif opcao == '5':
            media_duracao()
        elif opcao == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")