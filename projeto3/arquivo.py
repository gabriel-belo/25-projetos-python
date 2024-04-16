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

def descubra_computador():
    baixo= 1
    alto= 10
    feedback= ""
    num= int(input('Escolha o número: '))
    tentativa=0
    while num != tentativa:
        tentativa= random.randint(1, 10)
        feedback= input(f"A tentativa {tentativa} é muito alta (A) ou muito baixa (B):  ").upper()
        if feedback == "A":
            alto= tentativa -1
        elif feedback == "B":
            baixo= tentativa + 1
    print("Parabéns, você acertou o número")


if __name__ == '__main__':
    descubra_computador()