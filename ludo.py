import random

CASA_FINAL = 30


def rolar_dado():
    return random.randint(1, 6)


def mostrar_posicoes(posicoes):
    print("\nPosições: ")
    for indice, pos in enumerate(posicoes, start=1):
        estado = "Casa inicial" if pos == 0 else f"Casa {pos}"
        print(f"Jogador {indice}: {estado}")
    print()


def jogar_turno(nome, posicao_atual, posicao_oponente):
    print(f"-- Turno de {nome} --")
    input("Pressione Enter para rolar o dado...")
    valor = rolar_dado()
    print(f"{nome} rolou: {valor}")

    ganhou_turno_extra = False
    if posicao_atual == 0:
        if valor == 6:
            posicao_atual = 1
            ganhou_turno_extra = True
            print(f"{nome} saiu da casa inicial e entrou no tabuleiro!")
        else:
            print(f"{nome} precisa de 6 para sair da casa inicial.")
            return posicao_atual, posicao_oponente, False
    else:
        posicao_atual += valor
        if posicao_atual > CASA_FINAL:
            posicao_atual = CASA_FINAL
        print(f"{nome} avançou para a casa {posicao_atual}.")

    if posicao_atual == posicao_oponente and posicao_atual != 0:
        posicao_oponente = 0
        print(f"{nome} capturou o adversário! O outro jogador volta para a casa inicial.")

    if valor == 6:
        ganhou_turno_extra = True
        print(f"{nome} ganhou outro turno por ter rolado 6!")

    return posicao_atual, posicao_oponente, ganhou_turno_extra


def main():
    posicoes = [0, 0]
    nomes = ["Jogador 1", "Jogador 2"]
    vez = 0

    print("Bem-vindo ao Ludo!")
    print(f"Meta: chegar à casa {CASA_FINAL}")

    while True:
        mostrar_posicoes(posicoes)
        pos, outro, ganhou_turno_extra = jogar_turno(nomes[vez], posicoes[vez], posicoes[1 - vez])
        posicoes[vez] = pos
        posicoes[1 - vez] = outro

        if posicoes[vez] == CASA_FINAL:
            print(f"\n{nomes[vez]} venceu o jogo! Parabéns!")
            break

        if not ganhou_turno_extra:
            vez = 1 - vez

    print("Fim de jogo.")


if __name__ == "__main__":
    main()
