from tabuleiro_cash import MostrarTabuleiro
#from movimentar_pecasBETA import *
from MovimentarPecas import *


partida = True
jogador = True
jogador_pecas_azul = ["\033[0;36;1mt\033[m","\033[0;36;1mc\033[m","\033[0;36;1mr\033[m","\033[0;36;1md\033[m","\033[0;36;1mb\033[m","\033[0;36;1mp\033[m"]
jogador_pecas_vermelho = ["\033[0;31;1mT\033[m","\033[0;31;1mC\033[m","\033[0;31;1mR\033[m","\033[0;31;1mD\033[m","\033[0;31;1mB\033[m","\033[0;31;1mP\033[m"]





while partida:
    
    print(MostrarTabuleiro())
    

    if jogador == True:
         print("Jogador atual: Jogador 1")
    else:
        print("Jogador atual: Jogador 2")


    #inserindo e tratando os dados da posição final e inicial
    print(MostrarTabuleiro())
    posicao_inicial = input("digite a posição para selecionar  a aa peça: ")
    posicao_inicial = Tupla_posicao_inicial(posicao_inicial)


    #vai ter a def para mostrar onde ele pode jogar

    posicao_final= input('Digite a posicao para mover a peça: ')
    posicao_final = Tupla_posicao_final(posicao_final)

    #for que vai comparar se a tupla posicao final == vetor que vem da def para mostrar onde ele pode jogar


    #======================================
    


    if jogador == True:
        Pecas_do_jogador = jogador_pecas_azul
        for x in range (len(Pecas_do_jogador)):
            if tabuleiro[posicao_inicial[0]][posicao_inicial[1]] == Pecas_do_jogador[x]:
                
                print(Pecas_do_jogador[x])
            
                break
        else:
                print("Você só pode jogar com suas peças!")
    else:
        Pecas_do_jogador = jogador_pecas_vermelho
        for y in  range(len(Pecas_do_jogador)):
            if tabuleiro[posicao_inicial[0]][posicao_inicial[1]] == Pecas_do_jogador[y]:

                break
        else:
                print("Você só pode jogar com suas peças!")
        



    
    

   
   