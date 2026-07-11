def menu():
    print("Selecione a opção desejada (0 a 6):")
    print("0 - Adicionar filme (opcional)")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")

def adicionar_filme():
    titulo = input("Digite o título do filme: ")
    diretor = input("Digite o nome do diretor: ")
    genero = input("Digite o gênero do filme: ")
    duracao = input("Digite a duração do filme (em minutos): ")

    with open("filmes.txt", "a", encoding="utf-8") as f:
        f.write(f"{titulo},{diretor},{genero},{duracao}\n") 

# opção 1
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
    print(f"Quantidade total de filmes: {contador}\n")
    return contador

#opção 2
def info_por_titulo():
    titulo_busca = input("Digite o título do filme: ").strip().lower()
    filmes = ler_filmes()
    achou = False
    for filme in filmes:
        partes = filme.split(",")
        if len(partes) >= 4 and partes[0].strip().lower() == titulo_busca:
            print(f"Título: {partes[0].strip()}")
            print(f"Diretor: {partes[1].strip()}")
            print(f"Gênero: {partes[2].strip()}")
            print(f"Duração: {partes[3].strip()} minutos")
            achou = True
            break
    if not achou:
        print("Filme não encontrado.")
        
#opçaõ 3:
def filmes_por_diretor():
    diretor_busca = input("Digite o nome do diretor: ").strip().lower()
    filmes = ler_filmes()
    encontrados = False
    for filme in filmes:
        partes = filme.split(",")
        if len(partes) >= 4 and partes[1].strip().lower() == diretor_busca:
            print(filme)
            encontrados = True
    if not encontrados:
        print("Nenhum filme encontrado para este diretor.")


if __name__ == "__main__":
    while True:
        menu()
        opcao = input("Selecione a opção desejada (0 a 6): ").strip()
        if opcao == '0':
            adicionar_filme()
        elif opcao == '1':
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