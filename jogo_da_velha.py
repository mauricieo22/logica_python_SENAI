# jogo da velha com matrizes #exibir tabuleiro #verificar vitória #jogar

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro():
    print("\nTabuleiro:\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("---------")


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
        linha = int(input(f"\nJogador {jogador}, escolha a LINHA (0-2): ")) 
        coluna = int(input(f"Jogador {jogador}, escolha a COLUNA (0-2): "))
        
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

#jogar novamente ou encerrar o jogo
print()
print("Jogar novamente? (s/n)")
if input().lower() == "s":
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogar()
else:
    print("Fim do jogo!")