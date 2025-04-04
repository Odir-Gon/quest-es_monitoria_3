with open('questao3.txt', 'w'):
    pass
for x in range(3):
    with open('questao3.txt', 'a') as arquivo:
        escolha = input('1.Zona Norte \n'
                             '2.Zona Sul\n')
        arquivo.write(escolha + ',')
        escolha2 = input('Animal de Estimação? S/N')
        arquivo.write(escolha2 + '\n')

with open('questao3.txt', 'r') as arquivo:
    zs = 0
    zn = 0
    animal = 0
    sem_animal = 0
    zona_sul_animal = 0
    for linha in arquivo:
        partes = [parte.strip() for parte in linha.split(",")]
        if partes[0] == '1':
            zn += 1
        elif partes[0] == '2':
            zs += 1
        if partes[1] == 's':
            animal+= 1
        if partes[1] == 'n':
            sem_animal += 1
        if partes[0] == '2' and partes[1].strip().lower() == 's':
            zona_sul_animal += 1

print(f'Zona Sul Total: {zs}\n'
      f'Zona Norte Total: {zn}\n'
      f'Pets Total: {animal}\n'
      f'Zona Sul + Pet: {zona_sul_animal}\n')


# partes = [int(parte) for parte in linha.split(".")]