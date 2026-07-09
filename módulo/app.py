from conversoes import celsius_fahrenheit,  metros_quilometros

def main() -> None:
    #Exemplo de uso das funções de conversão
    c = 20
    f = 1500
    print(f"{c}°C = {celsius_fahrenheit(c):.2f}°F")
    print(f"{f} m = {metros_quilometros(f):.3f} km ")

#ponto de entrada do programa
#só executa main() se este arqivo for o scrit principal
if __name__ == "__main__":
    main()