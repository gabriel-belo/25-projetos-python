# Crie um programa em que o usuário ira escolher um número aleatório e o computador ira tentar acerta-lo
import random

# def descubra():

#     num= int(input('Escolha o número: '))
#     while True:
#         tentativa= random.randint(1,10)

#         if tentativa == num:
#             print("Parabéns, você acertou o número")
#             break
#         elif tentativa > num:
#             print("Seu chute foi alto")
#         elif tentativa < num:
#             print("Seu chute foi baixo")


# if __name__ == '__main__':
#     descubra()

def descubra_computador(x):
    minimo= 1
    maximo= x
    feedback= ""

    while feedback != 'C' :
        if minimo != maximo:
            tentativa= random.randint(minimo, maximo)
        else:
            tentativa= minimo
        feedback= input(f"A tentativa {tentativa} é muito alta (A), muito baixa (B) ou correta (C):  ").upper()
        if feedback == "A":
            maximo= tentativa -1
        elif feedback == "B":
            minimo= tentativa + 1
    print("Parabéns, você acertou o número")


if __name__ == '__main__':
    descubra_computador(20)