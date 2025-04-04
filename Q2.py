validos = []
invalidos = []

with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        partes = [int(parte) for parte in linha.split(".")]

        e_valido = True  
        for parte in partes:
            if not (0 <= parte <= 255):  
                e_valido = False
                break  

        if e_valido:
            validos.append(linha.strip())
        else:
            invalidos.append(linha.strip())

print(validos)
print(invalidos)

'''partes = []
for part in line.split("."):
    partes.append(int(part))'''
