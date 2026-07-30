import os

ARQUIVO_DADOS = 'filmes.txt'

# --- FUNÇÕES DE PROCESSAMENTO DE DADOS ---

def carregar_filmes(nome_arquivo):
    """Lê o arquivo .txt e retorna uma lista de dicionários."""
    filmes = []
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado. Crie o arquivo e tente novamente.")
        return filmes

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                # Divide a linha pelas vírgulas
                partes = linha.split(',')
                if len(partes) == 4:
                    filme = {
                        'titulo': partes[0].strip(),
                        'diretor': partes[1].strip(),
                        'genero': partes[2].strip(),
                        'duracao': int(partes[3].strip())
                    }
                    filmes.append(filme)
    return filmes

def quantidade_total(filmes):
    """1 - Retorna a quantidade total de filmes no arquivo."""
    return len(filmes)

def info_por_titulo(filmes, titulo_buscado):
    """2 - Busca e exibe as informações de um filme pelo título."""
    for filme in filmes:
        if filme['titulo'].lower() == titulo_buscado.lower():
            return filme
    return None

def filmes_por_diretor(filmes, diretor_buscado):
    """3 - Retorna uma lista de filmes de um diretor específico."""
    encontrados = []
    for filme in filmes:
        if filme['diretor'].lower() == diretor_buscado.lower():
            encontrados.append(filme['titulo'])
    return encontrados

def filmes_por_genero(filmes, genero_buscado):
    """4 - Retorna uma lista de filmes de um gênero específico."""
    encontrados = []
    for filme in filmes:
        if filme['genero'].lower() == genero_buscado.lower():
            encontrados.append(filme['titulo'])
    return encontrados

def media_de_duracao(filmes):
    """5 - Calcula a média de duração de todos os filmes."""
    if not filmes:
        return 0
    soma_duracao = sum(filme['duracao'] for filme in filmes)
    return soma_duracao / len(filmes)

# --- PROGRAMA PRINCIPAL (MENU) ---

def main():
    filmes = carregar_filmes(ARQUIVO_DADOS)
    
    if not filmes:
        return # Encerra se não houver dados
    
    while True:
        print("\n" + "="*35)
        print("         MENU DE FILMES")
        print("="*35)
        print("1 - Quantidade total de filmes")
        print("2 - Informações de um filme pelo título")
        print("3 - Filmes de um diretor específico")
        print("4 - Filmes de um gênero específico")
        print("5 - Média de duração dos filmes")
        print("6 - Sair")
        print("="*35)
        
        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == '1':
            total = quantidade_total(filmes)
            print(f"\n> O arquivo contém um total de {total} filmes.")
            
        elif opcao == '2':
            titulo = input("Digite o título do filme: ")
            info = info_por_titulo(filmes, titulo)
            if info:
                print(f"\n> Informações sobre '{info['titulo']}':")
                print(f"  Diretor: {info['diretor']}")
                print(f"  Gênero: {info['genero']}")
                print(f"  Duração: {info['duracao']} minutos")
            else:
                print("\n> Filme não encontrado no banco de dados.")
                
        elif opcao == '3':
            diretor = input("Digite o nome do diretor: ")
            lista = filmes_por_diretor(filmes, diretor)
            if lista:
                print(f"\n> Filmes dirigidos por {diretor}:")
                for f in lista:
                    print(f"  - {f}")
            else:
                print("\n> Nenhum filme encontrado para este diretor.")
                
        elif opcao == '4':
            genero = input("Digite o gênero (ex: Drama, Ficcão Científica): ")
            lista = filmes_por_genero(filmes, genero)
            if lista:
                print(f"\n> Filmes do gênero {genero}:")
                for f in lista:
                    print(f"  - {f}")
            else:
                print("\n> Nenhum filme encontrado para este gênero.")
                
        elif opcao == '5':
            media = media_de_duracao(filmes)
            print(f"\n> A média de duração dos filmes é de {media:.2f} minutos.")
            
        elif opcao == '6':
            print("\nEncerrando o programa. Até logo!")
            break
            
        else:
            print("\n> Opção inválida. Por favor, escolha um número de 1 a 6.")

if __name__ == "__main__":
    main()