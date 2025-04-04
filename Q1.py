def votacao():
    print("1. Star Wars \n"
          "2. Star Trek")

    for x in range(10):
        voto = input(f'Digite o voto {x + 1}\n')
        with open ("arquivo_q2.txt", "a") as arquivo:
            arquivo.write(voto + "\n")
    print("DONE!")

while True:
    escolha = int(input('1. Criar arquivo \n'
                        '2. Votação \n'
                        '3. Sair'))

    if escolha == 1:
        with open ("arquivo_q2.txt", "w") as arquivo:
            pass
        print("Criado.")
        break

    elif escolha == 2:
        wars = 0
        trek = 0
        votacao()
        with open("arquivo_q2.txt", "r") as arquivo:
            for line in arquivo:
                if line.strip() == "1":
                    wars += 1
                else:
                    trek += 1
            print(f"Star Wars : {wars}\n"
                  f"Star Trek : {trek}\n")
            with open("arquivo_q2.txt", "w") as file:
                pass
            break
    elif escolha == 3:
        break

