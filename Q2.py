validos = []
invalidos = []

with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        partes = [int(parte) for parte in linha.split(".")]

        # Check each part without using `all()`
        e_valido = True  # Assume the IP is valid
        for parte in partes:
            if not (0 <= parte <= 255):  # Check if any part is invalid
                e_valido = False
                break  # Exit the loop as soon as we find an invalid part

        if e_valido:
            validos.append(linha.strip())
        else:
            invalidos.append(linha.strip())

print(validos)
print(invalidos)

'''partes = []
for part in line.split("."):
    partes.append(int(part))'''