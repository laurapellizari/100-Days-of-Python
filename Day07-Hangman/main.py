#Day 07 - Hangman Game
import random


def jogar():
    mod = mens_abertura()
    palavra_secreta, letras_acertadas = mode_game(mod)

    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    acerto = False
    enforco = False
    flag = False
    erro = 0
    cc = 0
    life = 10
    size = len(palavra_secreta)
    chutes = []

    while (not enforco and not acerto):

        flag = control(flag, letras_acertadas)
        chute = input("Qual letra?\n")
        chute = chute.strip().upper()

        while (chute in chutes):
            print("Você já chutou essa! Tente outra: ")
            chute = input("Qual letra?\n")
            chute = chute.strip().upper()
            for let in letras:
                if(let == chute):
                    letras.remove(let)
        chutes.append(chute)

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                    cc = cc + 1
                index = index + 1
            print(letras_acertadas)
            print("CHUTES: ", chutes)
            print("LETRAS RESTANTES: ", letras)
            #       print(chutes_restantes)

            if (cc == size):
                acerto = True
                winner()
                print("A palavra era {}".format(palavra_secreta))

        else:
            life = life - 1
            erro = erro + 1
            print(letras_acertadas)
            #        print("Letras disponiveis: ")
            #         print(chutes_restantes)
            print("Letra errada! Restam {} chances".format(life))
            print("LETRAS RESTANTES: ", letras)
            print("CHUTES: ", chutes)
            desenha_forca(erro)
            if (life == 0):
                print("Você perdeu! A palavra era {}".format(palavra_secreta))
                loser()
                enforco = True


def mens_abertura():
    print("******************************")
    print("******* Bem vindo ************")
    print("******************************")

    print("Digite: ")
    mode = int(input("1. Para jogar contra o computador\n2. Para jogar multiplayer\n"))

    return mode


def mode_game(mode):
    arquivo = open('words.txt', "r")
    palavras = []
    letras_acertadas = []
    if (mode == 1):

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
        arquivo.close()
        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
    if (mode == 2):
        palavra_secreta = input("Digite uma palavra secreta: ")
        palavra_secreta = palavra_secreta.upper()
        pula()

    for letra in palavra_secreta:
        letras_acertadas.append("_")

    return palavra_secreta, letras_acertadas


def control(flag, letras_acertadas):
    if (flag == False):
        print(letras_acertadas)
        #    print("Letras disponiveis: ")
        #  print(chutes_restantes)
        flag = True


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    print(" |            ")
    print("_|___         ")
    print()


def loser():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def winner():
    print("Você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def pula():
    i = 0
    while (i < 30):
        print()
        i += 1

##################### The game #######################################
print('Welcome to the Hangman game')
jogar()