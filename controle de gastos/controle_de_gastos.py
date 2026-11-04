import json
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox


ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "movimentacoes.json")


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_dados():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(movimentacoes, arquivo, indent=4, ensure_ascii=False)


def atualizar_tela():
    lista.delete(0, tk.END)
    for item in sorted(movimentacoes, key=lambda item: item["id"]):
        lista.insert(
            tk.END,
            f"{item['id']} | {item['data']} | {item['tipo']} | "
            f"R$ {item['valor']:.2f} | {item['descricao']}",
        )

    receitas = sum(item["valor"] for item in movimentacoes if item["tipo"] == "Receita")
    despesas = sum(item["valor"] for item in movimentacoes if item["tipo"] == "Despesa")
    saldo.config(
        text=f"Receitas: R$ {receitas:.2f}   "
        f"Despesas: R$ {despesas:.2f}   Saldo: R$ {receitas - despesas:.2f}"
    )


def adicionar_movimentacao(tipo):
    descricao = campo_descricao.get().strip()
    if not descricao:
        messagebox.showerror("Erro", "Informe a descrição.")
        return

    try:
        valor = float(campo_valor.get().replace(",", "."))
        if valor <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Informe um valor maior que zero.")
        return

    data = campo_data.get().strip()
    if data:
        try:
            data = datetime.strptime(data, "%d/%m/%Y %H:%M").strftime("%d/%m/%Y %H:%M")
        except ValueError:
            messagebox.showerror("Erro", "Use a data no formato dd/mm/aaaa HH:MM.")
            return
    else:
        data = datetime.now().strftime("%d/%m/%Y %H:%M")

    movimentacoes.append(
        {
            "id": max((item["id"] for item in movimentacoes), default=0) + 1,
            "descricao": descricao,
            "valor": valor,
            "tipo": tipo,
            "data": data,
        }
    )
    try:
        salvar_dados()
    except OSError as erro:
        movimentacoes.pop()
        messagebox.showerror("Erro ao salvar", str(erro))
        return

    campo_descricao.delete(0, tk.END)
    campo_valor.delete(0, tk.END)
    campo_data.delete(0, tk.END)
    atualizar_tela()


def excluir_movimentacao():
    selecao = lista.curselection()
    if not selecao:
        messagebox.showwarning("Atenção", "Selecione uma movimentação para excluir.")
        return

    itens = sorted(movimentacoes, key=lambda item: item["id"])
    item = itens[selecao[0]]
    movimentacoes.remove(item)
    try:
        salvar_dados()
    except OSError as erro:
        movimentacoes.append(item)
        messagebox.showerror("Erro ao salvar", str(erro))
        atualizar_tela()
        return
    atualizar_tela()


def gerar_relatorio():
    receitas = sum(item["valor"] for item in movimentacoes if item["tipo"] == "Receita")
    despesas = sum(item["valor"] for item in movimentacoes if item["tipo"] == "Despesa")
    messagebox.showinfo(
        "Relatório financeiro",
        f"Total de receitas: R$ {receitas:.2f}\n"
        f"Total de despesas: R$ {despesas:.2f}\n"
        f"Saldo atual: R$ {receitas - despesas:.2f}\n"
        f"Quantidade de movimentações: {len(movimentacoes)}",
    )


try:
    movimentacoes = carregar_dados()
except (OSError, json.JSONDecodeError) as erro:
    messagebox.showerror("Erro", f"Não foi possível carregar os dados:\n{erro}")
    raise SystemExit(1)

janela = tk.Tk()
janela.title("Controle de Gastos")
janela.geometry("700x420")

tk.Label(janela, text="Controle de Gastos Pessoais", font=("Arial", 16)).pack(pady=10)

formulario = tk.Frame(janela)
formulario.pack(pady=5)

tk.Label(formulario, text="Descrição").grid(row=0, column=0)
tk.Label(formulario, text="Valor").grid(row=0, column=1)
tk.Label(formulario, text="Data (dd/mm/aaaa HH:MM)").grid(row=0, column=2)

campo_descricao = tk.Entry(formulario, width=22)
campo_descricao.grid(row=1, column=0, padx=4)
campo_valor = tk.Entry(formulario, width=12)
campo_valor.grid(row=1, column=1, padx=4)
campo_data = tk.Entry(formulario, width=22)
campo_data.grid(row=1, column=2, padx=4)

tk.Button(
    janela, text="Adicionar receita", command=lambda: adicionar_movimentacao("Receita")
).pack(pady=3)
tk.Button(
    janela, text="Adicionar despesa", command=lambda: adicionar_movimentacao("Despesa")
).pack(pady=3)

lista = tk.Listbox(janela, width=90, height=10)
lista.pack(padx=10, pady=8, fill="both", expand=True)

saldo = tk.Label(janela)
saldo.pack(pady=5)

botoes = tk.Frame(janela)
botoes.pack(pady=5)
tk.Button(botoes, text="Excluir selecionada", command=excluir_movimentacao).pack(
    side="left", padx=5
)
tk.Button(botoes, text="Gerar relatório", command=gerar_relatorio).pack(
    side="left", padx=5
)

atualizar_tela()
janela.mainloop()
