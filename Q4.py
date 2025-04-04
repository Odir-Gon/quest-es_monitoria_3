"""Crie  um  programa que tenha um menu de opções (sair, ler, escrever ou mostrar a média dos
valores  de  um  arquivo  .txt  ou  .csv).  Se  o  usuário  escolher  ler,  exibe  na  tela  o  conteúdo  do
arquivo. Se optar por escrever, escreva um número no arquivo. Se escolher média, exibe a média
de  todos  os  valores  do  arquivo.  Isso  em  um  loop  indefinido,  acaba  quando o usuário quiser
(escolher a opção sair).  """

while True:
    opcao = int(input('1. Escrever\n'
                      '2. Ler \n'
                      '3. Média\n'
                      '4. Apagar\n'
                      '5. Sair\n'))
    if opcao == 1:
        with open("arquivo4.txt", 'a') as arquivo:
            numero = input('digite um numero\n')
            arquivo.write(numero + "\n")
    elif opcao == 2:
        with open("arquivo4.txt" , 'r') as arquivo:
            for line in arquivo:
                print(line)
    elif opcao == 3:
        with open("arquivo4.txt", 'r') as arquivo:
            cont = 0
            soma  = 0
            for linha in arquivo:
                numero = float(linha.strip())
                cont += 1
                soma += numero
        media = soma / cont
        print(f"A média é {media}")
        with open("arquivo4.txt", 'r') as arquivo:
            for linha in arquivo:
                linha += linha
                cont +=1

    elif opcao == 4:
        with open ("arquivo4.txt", 'w') as arquivo:
            pass
    elif opcao == 5:
        break