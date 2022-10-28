import random


def jogar():
    titulo()

    forca = recebimento_palavra()

    palavra_secreta = forca.upper()
    palavra = ["_" for letra in palavra_secreta]

    enforcou = False
    ganhou = False
    erros = 0


    while(not enforcou and not ganhou):
        print(end="\n")
        print("-----------------------------")
        chute = pede_chute()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    palavra[index] = letra
                index += 1
        else:
            erros += 1
            desenha_forca(erros)
        enforcou = erros == 7
        ganhou = "_" not in palavra

        falta = palavra.count("_")
        print(palavra)
        print("Ainda falta", falta, "letra(s)")

    print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
    if(ganhou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def titulo():
    print(end="\n")
    print("****************************************".center(50))
    print("***Bem vindo ao nosso jogo de Forca!!***".center(50))
    print("****************************************".center(50))

def recebimento_palavra():
    with open("palavras.txt", "r") as arquivo:
        lista = []

        for palavra in arquivo:
            palavra = palavra.strip()
            lista.append(palavra)

        forca = lista[random.randrange(1, len(lista))]
        return forca

def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip(". ").upper()
    return chute

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("     _______________      ")
    print("    /               \     ")
    print("   /                 \    ")
    print("/\/                   \/\ ")
    print("\ |   XXXX     XXXX   | / ")
    print(" \|   XXXX     XXXX   |/  ")
    print("  |   XXX       XXX   |   ")
    print("  |                   |   ")
    print("  \__      XXX      __/   ")
    print("    |\     XXX     /|     ")
    print("    | |           | |     ")
    print("    | I I I I I I I |     ")
    print("    |  I I I I I I  |     ")
    print("    \_             _/     ")
    print("      \_         _/       ")
    print("        \_______/         ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!".center(50))
    print("       ___________      ".center(50))
    print("      '._==_==_=_.'     ".center(50))
    print("      .-\\:      /-.    ".center(50))
    print("     | (|:.     |) |    ".center(50))
    print("      '-|:.     |-'     ".center(50))
    print("        \\::.    /      ".center(50))
    print("         '::. .'        ".center(50))
    print("           ) (          ".center(50))
    print("         _.' '._        ".center(50))
    print("        '-------'       ".center(50))

def desenha_forca(erros):
    print("  _______     ".center(50))
    print(" |/      |    ".center(50))

    if(erros == 1):
        print(" |      (_)   ".center(50))
        print(" |            ".center(50))
        print(" |            ".center(50))
        print(" |            ".center(50))

    if(erros == 2):
        print(" |      (_)   ".center(50))
        print(" |       |    ".center(50))
        print(" |            ".center(50))
        print(" |            ".center(50))

    if(erros == 3):
        print(" |      (_)   ".center(50))
        print(" |      \|    ".center(50))
        print(" |            ".center(50))
        print(" |            ".center(50))

    if(erros == 4):
        print(" |      (_)   ".center(50))
        print(" |      \|/   ".center(50))
        print(" |            ".center(50))
        print(" |            ".center(50))

    if(erros == 5):
        print(" |      (_)   ".center(50))
        print(" |      \|/   ".center(50))
        print(" |       |    ".center(50))
        print(" |            ".center(50))

    if(erros == 6):
        print(" |      (_)   ".center(50))
        print(" |      \|/   ".center(50))
        print(" |       |    ".center(50))
        print(" |      /     ".center(50))

    if (erros == 7):
        print(" |      (_)   ".center(50))
        print(" |      \|/   ".center(50))
        print(" |       |    ".center(50))
        print(" |      / \   ".center(50))

    print(" |            ".center(50))
    print("_|___         ".center(50))
    print()


if(__name__ == "__main__"):
    jogar()