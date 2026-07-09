def calcular_media(lista):
    if len(lista) == 0:
        return 0  # Evita erro de divisão por zero
    return sum(lista) / len(lista)

notas = [7.5, 6.0, 9.5, 6.0]
media_final = calcular_media(notas)
print(f"A média é: {media_final}")