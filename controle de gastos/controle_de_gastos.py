import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO = "arquivo.json"

if os.path.exists(ARQUIVO):
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        try:
            movimentacoes = json.load(f)
        except json.JSONDecodeError:
            movimentacoes = []
else:
    movimentacoes = []


def salvar():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(movimentacoes, f, indent=4)

#opção 1
def adc_receita():
    descricao = input("Digite a descrição da receita: ")
    valor = float(input("Digite o valor da receita: "))
    data = input("Digite a data da receita (dd/mm/aaaa hh:mm): ")

    mov = {
        "id": len(movimentacoes) + 1,
        "descricao": descricao,
        "valor": valor,
        "tipo": "Receita",
        "data": data
    }

    movimentacoes.append(mov)
    salvar()
    print("\n-- Receita adicionada com sucesso! --\n")

#opção 2
def adc_despesa():
    descricao = input("Digite a descrição da despesa: ")
    valor = float(input("Digite o valor da despesa: "))
    data = input("Digite a data da despesa (dd/mm/aaaa hh:mm): ")

    mov = {
        "id": len(movimentacoes) + 1,
        "descricao": descricao,
        "valor": valor,
        "tipo": "Despesa",
        "data": data
    }

    movimentacoes.append(mov)
    salvar()
    print("\n-- Despesa adicionada com sucesso! --\n")

#Menu
while True:
    print("\n-----------MENU-----------")
    
    while True:
        print("1 - Adicionar Receita")
        print("2 - Adicionar Despesa")
        print("3 - Listar Movimentações")
        print("4 - Consultar Saldo")
        print("5 - Excluir Movimentação")
        print("6 - Gerar Relatório")
        print("7 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adc_receita()
        elif opcao == "2":
            adc_despesa()
        elif opcao == "3":
            list_mov()
        elif opcao == "4":
            consultar_saldo()
        elif opcao == "5":
            excluir_mov()
        elif opcao == "6":
            gerar_relatorio()
        elif opcao == "7":  
            print("\n--Saindo do programa!--")
            break    
        else:   
            print("\n--Opção inválida!--")