def fahrenheit_para_celsius(f):
    """Converte temperatura de Fahrenheit para Celsius """
    celsius = (f-32) *5/9
    return celsius

temp = 68
celsius = fahrenheit_para_celsius(temp)
print(f"{temp}ºF equivalem a {celsius:.2f}ºC")