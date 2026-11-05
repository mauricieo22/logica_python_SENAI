import json
import os
from datetime import datetime

ARQUIVO_PRODUTOS = "produtos.json"
ARQUIVO_MOVIMENTACOES = "movimentacoes.json"


#carrega os produtos salvos no arquivo .json
def carregar_produtos():
    try:
        with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, OSError):
        print("Erro ao ler o arquivo de produtos. Uma lista vazia será utilizada.")
        return []


#salva os produtos no arquivo .json
def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)


#carrega o histórico de entradas e saídas
def carregar_movimentacoes():
    try:
        with open(ARQUIVO_MOVIMENTACOES, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, OSError):
        print("Erro ao ler o histórico de movimentações.")
        return []


#guarda o histórico no arquivo .json
def salvar_movimentacoes(movimentacoes):
    with open(ARQUIVO_MOVIMENTACOES, "w", encoding="utf-8") as arquivo:
        json.dump(movimentacoes, arquivo, indent=4, ensure_ascii=False)


#procura o produto
def procurar_produto(produtos, codigo):
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None


def ler_inteiro(mensagem, minimo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print("Digite um número igual ou maior que", minimo)
            else:
                return valor
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_preco():
    while True:
        try:
            valor = float(input("Preço unitário: R$ ").replace(",", "."))
            if valor <= 0:
                print("O preço deve ser maior que zero.")
            else:
                return valor
        except ValueError:
            print("Digite um preço válido.")


#1 - cadastra o produto
def cadastrar_produto(produtos):
    print("\n ---CADASTRAR PRODUTO--- \n")
    codigo = ler_inteiro("Código: ", 1)

    if procurar_produto(produtos, codigo) is not None:
        print("Já existe um produto com esse código.")
        return

    nome = input("Nome do produto: ").strip()
    if nome == "":
        print("O nome é obrigatório.")
        return

    quantidade = ler_inteiro("Quantidade inicial: ", 0)
    minimo = ler_inteiro("Estoque mínimo: ", 0)
    preco = ler_preco()

    produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "estoque_minimo": minimo,
        "preco": preco
    }

    produtos.append(produto)
    salvar_produtos(produtos)
    print("Produto cadastrado com sucesso!")


# 2 - altera produtos
def alterar_produto(produtos):
    print("\n--- ALTERAR PRODUTO ---\n")
    codigo = ler_inteiro("Digite o código do produto: ", 1)
    produto = procurar_produto(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    print("Deixe o campo vazio para manter o valor atual.")
    nome = input(f"Nome ({produto['nome']}): ").strip()
    if nome != "":
        produto["nome"] = nome

    quantidade = input(f"Quantidade ({produto['quantidade']}): ").strip()
    if quantidade != "":
        try:
            quantidade = int(quantidade)
            if quantidade < 0:
                print("Quantidade não pode ser negativa. Valor mantido.")
            else:
                produto["quantidade"] = quantidade
        except ValueError:
            print("Quantidade inválida. Valor mantido.")

    minimo = input(f"Estoque mínimo ({produto['estoque_minimo']}): ").strip()
    if minimo != "":
        try:
            minimo = int(minimo)
            if minimo < 0:
                print("Estoque mínimo não pode ser negativo. Valor mantido.")
            else:
                produto["estoque_minimo"] = minimo
        except ValueError:
            print("Estoque mínimo inválido. Valor mantido.")

    preco = input(f"Preço (R$ {produto['preco']:.2f}): ").strip()
    if preco != "":
        try:
            preco = float(preco.replace(",", "."))
            if preco <= 0:
                print("O preço deve ser maior que zero. Valor mantido.")
            else:
                produto["preco"] = preco
        except ValueError:
            print("Preço inválido. Valor mantido.")

    salvar_produtos(produtos)
    print("Produto atualizado!")


#3 - excluir produtos
def excluir_produto(produtos):
    print("\n--- EXCLUIR PRODUTO ---\n")
    codigo = ler_inteiro("Digite o código do produto: ", 1)
    produto = procurar_produto(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    confirmar = input(f"Confirma a exclusão de {produto['nome']}? (s/n): ").lower()
    if confirmar == "s":
        produtos.remove(produto)
        salvar_produtos(produtos)
        print("Produto excluído.")
    else:
        print("Exclusão cancelada.")


#4 -listar produtos
def listar_produtos(produtos):
    print("\n--- LISTA DE PRODUTOS ---\n")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    print("-" * 75)
    print(f"{'Código':<10}{'Nome':<25}{'Quantidade':<12}{'Mínimo':<10}{'Preço':>12}")
    print("-" * 75)

    for produto in produtos:
        print(
            f"{produto['codigo']:<10}"
            f"{produto['nome']:<25}"
            f"{produto['quantidade']:<12}"
            f"{produto['estoque_minimo']:<10}"
            f"R$ {produto['preco']:>8.2f}"
        )
    print("-" * 75)


#5 e 6 - registra entrada e saída dos produtos
def registrar_movimentacao(produtos, movimentacoes, tipo):
    print(f"\n--- {tipo.upper()} DE MERCADORIAS ---\n")
    codigo = ler_inteiro("Código do produto: ", 1)
    produto = procurar_produto(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    quantidade = ler_inteiro("Quantidade: ", 1)

    if tipo == "Saída" and quantidade > produto["quantidade"]:
        print("Não há estoque suficiente para essa saída.")
        print("Quantidade disponível:", produto["quantidade"])
        return

    if tipo == "Entrada":
        produto["quantidade"] += quantidade
    else:
        produto["quantidade"] -= quantidade

    movimentacao = {
        "tipo": tipo,
        "codigo": codigo,
        "produto": produto["nome"],
        "quantidade": quantidade,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    movimentacoes.append(movimentacao)
    salvar_produtos(produtos)
    salvar_movimentacoes(movimentacoes)
    print(tipo, "registrada com sucesso!")


# 7 - consultar produto
def consultar_produto(produtos):
    print("\n--- CONSULTAR PRODUTO ---\n")
    print("1 - Consultar por código")
    print("2 - Consultar por nome")
    opcao = input("Escolha: ")

    encontrados = []

    if opcao == "1":
        codigo = ler_inteiro("Código: ", 1)
        produto = procurar_produto(produtos, codigo)
        if produto is not None:
            encontrados.append(produto)

    elif opcao == "2":
        nome = input("Digite o nome ou parte do nome: ").strip().lower()
        for produto in produtos:
            if nome in produto["nome"].lower():
                encontrados.append(produto)
    else:
        print("Opção inválida.")
        return

    if encontrados:
        listar_produtos(encontrados)
    else:
        print("Nenhum produto encontrado.")

#
# 8 -informa produtos com estoque baixo
def produtos_estoque_baixo(produtos):
    print("\n--- PRODUTOS COM ESTOQUE BAIXO ---")
    encontrados = []

    for produto in produtos:
        if produto["quantidade"] <= produto["estoque_minimo"]:
            encontrados.append(produto)

    if not encontrados:
        print("Não existem produtos com estoque baixo.")
        return

    print(f"{'Código':<10}{'Produto':<25}{'Quantidade':<15}{'Mínimo':<10}")
    for produto in encontrados:
        print(
            f"{produto['codigo']:<10}"
            f"{produto['nome']:<25}"
            f"{produto['quantidade']:<15}"
            f"{produto['estoque_minimo']:<10}"
        )

#9 - relatório das movimentaçoes
def relatorio_movimentacoes(movimentacoes):
    print("\n--- RELATÓRIO DE MOVIMENTAÇÕES ---")
    if len(movimentacoes) == 0:
        print("Nenhuma movimentação registrada.")
        return

    for mov in movimentacoes:
        print(
            f"{mov['data']} | {mov['tipo']} | "
            f"Código: {mov['codigo']} | {mov['produto']} | "
            f"Quantidade: {mov['quantidade']}"
        )


def menu():
    produtos = carregar_produtos()
    movimentacoes = carregar_movimentacoes()

    while True:
        print("\n========== CONTROLE DE ESTOQUE ==========")
        print("1 - Cadastrar produto")
        print("2 - Alterar produto")
        print("3 - Excluir produto")
        print("4 - Listar produtos")
        print("5 - Registrar entrada")
        print("6 - Registrar saída")
        print("7 - Consultar produto")
        print("8 - Produtos com estoque baixo")
        print("9 - Relatório de movimentações")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                cadastrar_produto(produtos)
            elif opcao == "2":
                alterar_produto(produtos)
            elif opcao == "3":
                excluir_produto(produtos)
            elif opcao == "4":
                listar_produtos(produtos)
            elif opcao == "5":
                registrar_movimentacao(produtos, movimentacoes, "Entrada")
            elif opcao == "6":
                registrar_movimentacao(produtos, movimentacoes, "Saída")
            elif opcao == "7":
                consultar_produto(produtos)
            elif opcao == "8":
                produtos_estoque_baixo(produtos)
            elif opcao == "9":
                relatorio_movimentacoes(movimentacoes)
            elif opcao == "0":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except (OSError, json.JSONDecodeError) as erro:
            print("Ocorreu um erro ao acessar os arquivos:", erro)


# inicia o programa
if __name__ == "__main__":
    menu()