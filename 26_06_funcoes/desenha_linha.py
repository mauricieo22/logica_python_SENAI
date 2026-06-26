# Praticando - Menu
# Com base no exercício anterior, construa uma estrutura de menus com os seguintes itens: Usuário, Clientes, Fornecedores, Relatórios

def desenha_linha(limite, preenchimento, largura):
    print(limite + (preenchimento * (largura - 2)) +limite)

lista = ["Usuário","Clientes", "Fornecedores", "Relatórios"]

colunas = 20
linhas = 1

print("--------MENU--------")

desenha_linha("+", "-", colunas)

for l in range(linhas):
    desenha_linha("|", " ", colunas)

desenha_linha("+", "-", colunas)