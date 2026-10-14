
import os

ARQUIVO = "contas.txt"
contas = {}

#carregar contas salvas
if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            if len(dados) == 3:
                contas[dados[0]] = {
                    "senha": dados[1],
                    "saldo": float(dados[2])
                }


def salvar():
    with open(ARQUIVO, "w") as arquivo:
        for conta, dados in contas.items():
            arquivo.write(
                f"{conta};{dados['senha']};{dados['saldo']}\n"
            )


def login():
    global conta_atual

    conta = input("Digite sua conta: ").strip()
    senha = input("Digite sua senha: ").strip()

    if conta == "" or senha == "":
        print("Conta e senha são obrigatórias.")
        return False

    if conta in contas:
        if contas[conta]["senha"] == senha:
            conta_atual = conta
            print("Login realizado com sucesso!")
            return True
        else:
            print("Senha incorreta.")
            return False

    #criar nova conta
    contas[conta] = {
        "senha": senha,
        "saldo": 1000.00
    }

    salvar()
    conta_atual = conta

    print("Conta criada com sucesso!")
    print("Saldo inicial: R$ 1.000,00")
    return True

#1 - consultar saldo
def consultar():
    print(f"Saldo: R$ {contas[conta_atual]['saldo']:.2f}")

#2- depositar
def depositar():
    valor = float(input("Valor do depósito: R$ "))

    if valor <= 0:
        print("Valor inválido.")
    else:
        contas[conta_atual]["saldo"] += valor
        salvar()
        print("Depósito realizado!")
        consultar()

#3- sacar
def sacar():
    valor = float(input("Valor do saque: R$ "))

    if valor <= 0:
        print("Valor inválido.")
    elif valor > contas[conta_atual]["saldo"]:
        print("Saldo insuficiente.")
    elif valor != int(valor):
        print("O caixa só trabalha com valores inteiros em reais.")
    else:
        restante = int(valor)
        contas[conta_atual]["saldo"] -= valor
        salvar()

        print("Saque realizado!")
        for cedula in [100, 50, 20, 10, 5, 2, 1]:
            quantidade = restante // cedula
            if quantidade > 0:
                print(f"{quantidade} cédula(s) de R$ {cedula}")
                restante %= cedula

        consultar()


# programa principal
while True:
    print("\n -- CAIXA ELETRÔNICO -- ")

    if not login():
        continue

    while True:
        print("\n1 - Consultar saldo")
        print("2 - Sacar")
        print("3 - Depositar")
        print("4 - Sair da conta")

        opcao = input("Escolha: ")

        if opcao == "1":
            consultar()
        elif opcao == "2":
            sacar()
        elif opcao == "3":
            depositar()
        elif opcao == "4":
            salvar()
            print("Você saiu da conta.")
            break
        else:
            print("Opção inválida.")
