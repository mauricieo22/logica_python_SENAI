def menu():
    print("Selecione a opção desejada (0 a 6):")
    print("0 - Adicionar filme (opcional)")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")

#opção 0:
def adicionar_filme():
    titulo = input("Digite o título do filme: ")
    ano = input("Digite o ano de lançamento: ")
    diretor = input("Digite o nome do diretor: ")
    genero = input("Digite o gênero do filme: ")
    duracao = input("Digite a duração do filme (em minutos): ") .strip()

    with open("filmes.txt", "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(f"Título: {titulo}\n")
        f.write(f"Ano: {ano}\n")
        f.write(f"Diretor: {diretor}\n")
        f.write(f"Gênero: {genero}\n")
        f.write(f"Duração: {duracao} minutos\n")
    print("\nFILME ADICIONADO!\n")

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
    encontrado = False
    try:
        with open ("filmes.txt", encoding="utf-8") as f:
            for linha in f:
                if linha.strip().startswith ("Título: "):
                    titulo = linha.split(":",1) [1].strip()
                    if titulo.lower() == titulo_busca:
                        print(f"Título: {titulo}")
                        try:
                            ano = next(f).strip()
                            diretor = next(f).strip()
                            genero = next(f).strip()
                            duracao =  next(f).strip()
                        except StopIteration:
                            print("Registro incompleto para esse título.")
                            return

                    print(ano)
                    print(diretor)
                    print(genero)
                    print(duracao)
                    encontrado = True
                    return
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return
    
    if not encontrado:
        print("Filme não encontrado.")

        
#opçaõ 3:
def filmes_por_diretor():
    diretor_busca = input("Digite o nome do diretor: ").strip().lower()
    contador = 0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            ultimo_titulo = ""
            for linha in f:
                s = linha.strip()
                if s.startswith("Título:"):
                    ultimo_titulo = s.split(":", 1) [1]. strip()
                elif s.startswith("Diretor:"):
                    diretor = s.split(":",1) [1] .strip()
                    if diretor.lower == diretor_busca:
                        contador += 1
                        print(f"- {ultimo_titulo}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado")
        return
    print(f"Total de filmes do direto {diretor_busca}: {contador}")
    return contador



#opçaõ 4:
def filmes_por_genero():
    genero_busca = input("Digite o gênero: ").strip().lower()
    contador = 0
    with open("filmes.txt", encoding="utf-8") as f:
        ultimo_titulo = ""
        for linha in f:
            s = linha.strip()
            if s.startswith("Título:"):
                ultimo_titulo = s.split(":", 1) [1]. strip()
            elif s.startswith("Diretor:"):
                genero = s.split(":",1) [1] .strip()
            if genero.lower() == genero_busca:
                contador += 1
                print(f"- {ultimo_titulo} ({genero})")

    
    print(f"Total de filmes por gênero: {genero_busca}: {contador}\n")


#opção 5:
def media_duracao():
    soma = 0
    cont = 0

    try:
        with open("Filmes.txt", encoding = "utf-8") as f:
            for linha in f:
                s = linha.srip()
                if s.startswith("Duração:"):
                    try:
                        minutos = int(s.split(":", 1)[1].strip().split()[0])
                    except (ValueError, IndexError):
                        #Ignora valores inválidos e continua
                        continue
                    soma += minutos
                    cont += 1
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não encontrado.")
        return 0
    if cont == 0:
        print("Nenhum filme encontrado.")
        return 0
    return soma / cont

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