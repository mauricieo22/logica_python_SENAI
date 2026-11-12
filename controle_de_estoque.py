import json
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, simpledialog, ttk

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


# carrega o histórico de entradas e saídas
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


class ControleEstoqueApp:
        def __init__(self, janela):
            self.janela = janela
            self.janela.title("SENAI | Controle de Estoque")
            self.janela.geometry("980x600")
            self.janela.minsize(760, 480)
            self.janela.configure(bg="#f2f5f4")
            self.produtos = carregar_produtos()
            self.movimentacoes = carregar_movimentacoes()
            self.filtrar_baixo = False
            ttk.Style().theme_use("clam")

            topo = tk.Frame(janela, bg="#164e52", padx=22, pady=17)
            topo.pack(fill="x")
            tk.Label(topo, text="CONTROLE DE ESTOQUE", bg="#164e52", fg="white",
                     font=("Segoe UI", 18, "bold")).pack(anchor="w")
            tk.Label(topo, text="Produtos e movimentações", bg="#164e52", fg="#cde5df",
                     font=("Segoe UI", 10)).pack(anchor="w")

            acoes = tk.Frame(janela, bg="#f2f5f4", padx=18, pady=13)
            acoes.pack(fill="x")
            comandos = [("Cadastrar", self.cadastrar), ("Alterar", self.alterar),
                        ("Excluir", self.excluir), ("Entrada", lambda: self.movimentar("Entrada")),
                        ("Saída", lambda: self.movimentar("Saída")),
                        ("Estoque baixo", self.alternar_filtro), ("Movimentações", self.relatorio)]
            for texto, comando in comandos:
                ttk.Button(acoes, text=texto, command=comando).pack(side="left", padx=(0, 6))

            busca = tk.Frame(janela, bg="#f2f5f4", padx=18, pady=0)
            busca.pack(fill="x")
            tk.Label(busca, text="Consultar", bg="#f2f5f4", font=("Segoe UI", 10, "bold")).pack(side="left", padx=(0, 8))
            self.termo = tk.StringVar()
            campo_busca = ttk.Entry(busca, textvariable=self.termo, width=35)
            campo_busca.pack(side="left")
            campo_busca.bind("<KeyRelease>", lambda _evento: self.atualizar())
            ttk.Button(busca, text="Limpar", command=self.limpar_busca).pack(side="left", padx=7)

            area = tk.Frame(janela, bg="#f2f5f4", padx=18)
            area.pack(fill="both", expand=True)
            colunas = ("codigo", "nome", "quantidade", "minimo", "preco", "situacao")
            self.tabela = ttk.Treeview(area, columns=colunas, show="headings")
            titulos = ("Código", "Produto", "Quantidade", "Qntd Mínima", "Preço unitário", "Situação")
            larguras = (80, 280, 110, 90, 130, 130)
            for coluna, titulo, largura in zip(colunas, titulos, larguras):
                self.tabela.heading(coluna, text=titulo)
                self.tabela.column(coluna, width=largura, anchor="w")
            self.tabela.tag_configure("baixo", foreground="#b54735")
            barra = ttk.Scrollbar(area, orient="vertical", command=self.tabela.yview)
            self.tabela.configure(yscrollcommand=barra.set)
            self.tabela.pack(side="left", fill="both", expand=True)
            barra.pack(side="right", fill="y")
            self.tabela.bind("<Double-1>", lambda _evento: self.alterar())
            self.status = tk.StringVar()
            tk.Label(janela, textvariable=self.status, bg="#e4ece9", fg="#344b4b",
                     anchor="w", padx=18, pady=8).pack(fill="x", pady=(10, 0))
            self.atualizar()

        def atualizar(self):
            for item in self.tabela.get_children():
                self.tabela.delete(item)
            termo = self.termo.get().strip().lower()
            baixos = 0
            exibidos = 0
            for produto in self.produtos:
                baixo = produto["quantidade"] <= produto["estoque_minimo"]
                baixos += int(baixo)
                if self.filtrar_baixo and not baixo:
                    continue
                if termo and termo not in str(produto["codigo"]) and termo not in produto["nome"].lower():
                    continue
                self.tabela.insert("", "end", iid=str(produto["codigo"]), values=(
                    produto["codigo"], produto["nome"], produto["quantidade"],
                    produto["estoque_minimo"], f"R$ {produto['preco']:.2f}",
                    "Estoque baixo" if baixo else "Disponível"
                ), tags=("baixo",) if baixo else ())
                exibidos += 1
            filtro = " | filtro de estoque baixo" if self.filtrar_baixo else ""
            self.status.set(f"{exibidos} produto(s) exibido(s) | {baixos} com estoque baixo{filtro}")

        def limpar_busca(self):
            self.termo.set("")
            self.atualizar()

        def selecionado(self):
            selecao = self.tabela.selection()
            if not selecao:
                messagebox.showinfo("Seleção", "Selecione um produto na tabela.", parent=self.janela)
                return None
            return procurar_produto(self.produtos, int(selecao[0]))

        def salvar(self):
            try:
                salvar_produtos(self.produtos)
                salvar_movimentacoes(self.movimentacoes)
                self.atualizar()
                return True
            except OSError as erro:
                messagebox.showerror("Erro ao salvar", str(erro), parent=self.janela)
                return False

        def formulario(self, produto=None):
            janela = tk.Toplevel(self.janela)
            janela.title("Alterar produto" if produto else "Cadastrar produto")
            janela.resizable(False, False)
            janela.transient(self.janela)
            janela.grab_set()
            dados = [("Código", "codigo", produto["codigo"] if produto else ""),
                     ("Nome", "nome", produto["nome"] if produto else ""),
                     ("Quantidade", "quantidade", produto["quantidade"] if produto else "0"),
                     ("Estoque mínimo", "estoque_minimo", produto["estoque_minimo"] if produto else "0"),
                     ("Preço unitário", "preco", produto["preco"] if produto else "")]
            quadro = tk.Frame(janela, padx=18, pady=16)
            quadro.pack()
            campos = {}
            for linha, (rotulo, chave, valor) in enumerate(dados):
                tk.Label(quadro, text=rotulo).grid(row=linha, column=0, sticky="w", padx=(0, 10), pady=5)
                campo = ttk.Entry(quadro, width=28)
                campo.insert(0, str(valor))
                campo.grid(row=linha, column=1, pady=5)
                campos[chave] = campo
                if produto and chave == "codigo":
                    campo.configure(state="disabled")

            def confirmar():
                try:
                    codigo = int(campos["codigo"].get())
                    nome = campos["nome"].get().strip()
                    quantidade = int(campos["quantidade"].get())
                    minimo = int(campos["estoque_minimo"].get())
                    preco = float(campos["preco"].get().replace(",", "."))
                    if codigo < 1 or not nome or quantidade < 0 or minimo < 0 or preco <= 0:
                        raise ValueError
                except ValueError:
                    messagebox.showerror("Dados inválidos", "Confira os campos e tente novamente.", parent=janela)
                    return
                if produto is None:
                    if procurar_produto(self.produtos, codigo):
                        messagebox.showerror("Código existente", "Já existe um produto com esse código.", parent=janela)
                        return
                    self.produtos.append({"codigo": codigo, "nome": nome, "quantidade": quantidade,
                                          "estoque_minimo": minimo, "preco": preco})
                else:
                    produto.update(nome=nome, quantidade=quantidade, estoque_minimo=minimo, preco=preco)
                if self.salvar():
                    janela.destroy()

            botoes = ttk.Frame(quadro)
            botoes.grid(row=len(dados), column=0, columnspan=2, sticky="e", pady=(12, 0))
            ttk.Button(botoes, text="Cancelar", command=janela.destroy).pack(side="left", padx=4)
            ttk.Button(botoes, text="Salvar", command=confirmar).pack(side="left")

        def cadastrar(self):
            self.formulario()

        def alterar(self):
            produto = self.selecionado()
            if produto:
                self.formulario(produto)

        def excluir(self):
            produto = self.selecionado()
            if produto and messagebox.askyesno("Excluir produto", f"Excluir {produto['nome']}?", parent=self.janela):
                self.produtos.remove(produto)
                self.salvar()

        def movimentar(self, tipo):
            produto = self.selecionado()
            if not produto:
                return
            quantidade = simpledialog.askinteger(tipo, f"Quantidade para {tipo.lower()} de {produto['nome']}:",
                                                 parent=self.janela, minvalue=1)
            if quantidade is None:
                return
            if tipo == "Saída" and quantidade > produto["quantidade"]:
                messagebox.showerror("Estoque insuficiente", f"Disponível: {produto['quantidade']}.", parent=self.janela)
                return
            produto["quantidade"] += quantidade if tipo == "Entrada" else -quantidade
            self.movimentacoes.append({"tipo": tipo, "codigo": produto["codigo"], "produto": produto["nome"],
                                       "quantidade": quantidade, "data": datetime.now().strftime("%d/%m/%Y %H:%M")})
            if self.salvar():
                messagebox.showinfo("Movimentação", f"{tipo} registrada com sucesso.", parent=self.janela)

        def alternar_filtro(self):
            self.filtrar_baixo = not self.filtrar_baixo
            self.atualizar()

        def relatorio(self):
            janela = tk.Toplevel(self.janela)
            janela.title("Relatório de movimentações")
            janela.geometry("720x400")
            colunas = ("data", "tipo", "codigo", "produto", "quantidade")
            tabela = ttk.Treeview(janela, columns=colunas, show="headings")
            for coluna, titulo in zip(colunas, ("Data", "Tipo", "Código", "Produto", "Quantidade")):
                tabela.heading(coluna, text=titulo)
                tabela.column(coluna, width=130 if coluna != "produto" else 220, anchor="w")
            for mov in reversed(self.movimentacoes):
                tabela.insert("", "end", values=(mov["data"], mov["tipo"], mov["codigo"], mov["produto"], mov["quantidade"]))
            tabela.pack(fill="both", expand=True, padx=12, pady=12)
            if not self.movimentacoes:
                tk.Label(janela, text="Nenhuma movimentação registrada.").place(relx=0.5, rely=0.5, anchor="center")


def abrir_interface():
    janela = tk.Tk()
    ControleEstoqueApp(janela)
    janela.mainloop()


def alterar_produto(produtos):
    print("\n--- ALTERAR PRODUTO ---\n")
    codigo = ler_inteiro("Digite o código do produto: ", 1)
    produto = procurar_produto(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    print("Deixe o campo vazio para manter o valor atual.")
    nome = input(f"Nome ({produto['nome']}): ").strip()
    if nome:
        produto["nome"] = nome

    quantidade = input(f"Quantidade ({produto['quantidade']}): ").strip()
    if quantidade:
        try:
            quantidade = int(quantidade)
            if quantidade < 0:
                print("Quantidade não pode ser negativa. Valor mantido.")
            else:
                produto["quantidade"] = quantidade
        except ValueError:
            print("Quantidade inválida. Valor mantido.")

    minimo = input(f"Estoque mínimo ({produto['estoque_minimo']}): ").strip()
    if minimo:
        try:
            minimo = int(minimo)
            if minimo < 0:
                print("Estoque mínimo não pode ser negativo. Valor mantido.")
            else:
                produto["estoque_minimo"] = minimo
        except ValueError:
            print("Estoque mínimo inválido. Valor mantido.")

    preco = input(f"Preço (R$ {produto['preco']:.2f}): ").strip()
    if preco:
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


def menu_terminal():
    produtos = carregar_produtos()
    movimentacoes = carregar_movimentacoes()

    while True:
        
        print("\n    -- CONTROLE DE ESTOQUE --            ")
        print("---------------------------------")
        print("|1 - Cadastrar produto          |")
        print("|2 - Alterar produto            |")
        print("|3 - Excluir produto            |")
        print("|4 - Listar produtos            |")
        print("|5 - Registrar entrada          |")
        print("|6 - Registrar saída            |")
        print("|7 - Consultar produto          |")
        print("|8 - Produtos com estoque baixo |")
        print("|9 - Relatório de movimentações |")
        print("|0 - Sair                       |")
        print("---------------------------------")

        opcao = input("\nEscolha uma opção: ")

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
def menu():
    abrir_interface()


if __name__ == "__main__":
    menu()