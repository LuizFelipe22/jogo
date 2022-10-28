import forca
import Adiviacao

print(end="\n")
print("****************************************".center(50))
print("******Qual jogo você deseja jogar?******".center(50))
print("****************************************".center(50))
print(end="\n")

jogo = int(input("Digite (1) para Adivinhação ou (2) para jogar Forca: "))

if(jogo == 1):
    print("Então vamos jogar Adivinhação!!!")
    Adiviacao.jogar()
elif(jogo == 2):
    print ("Então vamos jogar forca!!!")
    forca.jogar()