nomes = []
for i in range(3):
    nome = input(f"Insira o nome {i+1}: ")
    if nome == "":
        break
    nomes.append(nome)

with open("nomes.txt", "w", encoding= "utf-8") as f:               # encoding="utf-8" para não ocorrer erro sobre a acentuação
    for nome in nomes:
        f.write(nome + "\n")