#Densenvolva um jogo de pedra papel  tesoura
import json
import os
import random as rd
for i in range(1000):
    print("-" * 15)
    try:
        if os.path.exists('projeto4/arquivo.py'):
                with open('projeto4/arquivo.py', 'r') as arquivo:
                    lista= json.load(arquivo)
        else:
            lista=[]
            
        lista=['pedra', 'tesoura', 'papel']
        dic={}
        cont1=0
        cont2=0
        empates=0
        # jogador1= input("Escolha pedra papel ou tesoura: ")
        jogador1= rd.choice(lista)
        jogador2= rd.choice(lista)

        if jogador1 == jogador2:
            print("Empate")
            empates+=1
        elif jogador1.index(1) == jogador2.index(2):
            print("Jogador 1 ganhou!")
            cont1+=1
        elif jogador1.index(2) == jogador2.index(3):
            print("Jogador 1 ganhou!")
            cont1+=1
        elif jogador1.index(3) == jogador2.index(1):
            print("Jogador 1 ganhou!")
            cont1+=1
        else:
            print("Jogador 2 ganhou!")
            cont2+=1
        
        dic['empates']=empates
        dic['jogador 1']=cont1
        dic['jogador 2']=cont2
        lista.append(dic)
        
        with open('projeto4/arquivo.py', 'w', encoding='utf-8') as arquivo:       # gera arquivo json
                json.dump(lista, arquivo, indent=4)
        

    except FileNotFoundError:
            print('ERRO. O arquivo não foi encontrado')

print(lista[len(lista)-1])

