# Crie um programa em que o computador ira escolher um número aleatório e tente acerta-lo
import random

def descubra():
    num= random.randint(1,10)
    while True:
        tentativa= int(input('Tente acertar o número: '))

        if tentativa == num:
            print("Parabéns, você acertou o número")
            break
        elif tentativa > num:
            print("Seu chute foi alto")
        elif tentativa < num:
            print("Seu chute foi baixo")
        else:
            print("Você errou o número, tente mais uma vez")


if __name__ == '__main__':
    descubra()