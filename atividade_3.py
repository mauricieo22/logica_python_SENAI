senha = input("Digite sua senha: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in senha:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True
    if not ch.isalnum(): #alfanúmerico
        has_special = True

errors = []
if len(senha) < 8:
    errors.append("Minímo 8 caracteres!")
if not has_upper:
    errors.append("Pelo menos uma letra maiúscula.")
if not has_lower:
    errors.append("Pelo menos uma letra minúscula.")
if not has_digit:
    errors.append("Pelo menos um dígito.")
if not has_special:
    errors.append("Pelo menos um caractere especial.")

if errors:
    print("Senha fraca!")
for e in errors:
    print(e)
else:
    print("Senha forte!")