import random

def jogar():
    print(end="\n")
    print("****************************************".center(50))
    print("*Bem vindo ao nosso jogo de adivinhação*".center(50))
    print("****************************************".center(50))
    print(end="\n")

    Numero_secreto = random.randrange(1, 101)
    numero_de_tentativas = 0
    pontos = 1000

    nivel = int(input("Escolha a dificuldade: Nível(1) Nível(2) Nível(3): "))
    if(nivel == 1):
        numero_de_tentativas = 20
        print("<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>".center(50))
        print("Você tem", numero_de_tentativas, "chances para acertar o número secreto")
    elif(nivel == 2):
        numero_de_tentativas = 10
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Você tem", numero_de_tentativas, "chances para acertar o número secreto")
    else:
        numero_de_tentativas = 5
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Você tem", numero_de_tentativas, "chances para acertar o número secreto")

    for tentativas in range(1, numero_de_tentativas + 1):
        print("{} de {} tentativas".format(tentativas, numero_de_tentativas))
        print(end="\n")
        chute = input("Digite um número entre 1 e 100: ")
        Nu = int(chute)

        if(Nu < 1):
            print("Este número não estar entre 1 e 100")
            continue
        if(Nu > 100):
            print("Este número não estar entre 1 e 100")
            continue

        print(end="\n")
        print("Você digitou", chute)

        Acertou    = Numero_secreto == Nu
        ChuteMaior = Numero_secreto < Nu
        ChuteMenor = Numero_secreto > Nu

        if(Acertou):
            print("Parabéns, você acertou!")
            print("_______________________")
            break
        else:
            if(ChuteMaior):
                print("Você errou pra cima!!")
                print("_____________________")
            elif (ChuteMenor):
                print("Você errou para baixo!!")
                print("_______________________")
            pontos_perd = abs(tentativas - numero_de_tentativas)
            pontos = pontos - pontos_perd
    print(end="\n")
    print("Você terminou a partida com", pontos, "pontos")
    print("Fim de jogo")
    print(end="\n")
    print("O número secreto era", Numero_secreto)

if(__name__ == "__main__"):
    jogar()