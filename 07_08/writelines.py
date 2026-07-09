linhas = ["Linha 1 \n",
          "Linha 2 \n",
          "Linha 3 \n"]
with open("saida_lines.txt", "w") as f:
    f.writelines(linhas)