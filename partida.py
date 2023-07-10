from tabuleiro import tabuleiro_jogo
from movimentar_pecasBETA import *

jogador = True
Pecadojogador = ["\033[0;36;1mt\033[m","\033[0;36;1mc\033[m","\033[0;36;1mr\033[m","\033[0;36;1md\033[m","\033[0;36;1mb\033[m","\033[0;36;1mp\033[m"]
Pecadojogador1 = ["\033[0;31;1mT\033[m","\033[0;31;1mC\033[m","\033[0;31;1mR\033[m","\033[0;31;1mD\033[m","\033[0;31;1mB\033[m","\033[0;31;1mP\033[m"]




while True:
    print(tabuleiro_jogo())
    if jogador == True:
        print("Jogador 1")
        posicao_inicial = input("digite a posição para selecionar  a aa peça: ")
        posicao_final= input('Digite a posicao para mover a peça: ')
        cash = posicao_inicial
        cash = PosicaoInicial(cash)
        for x in range (len(Pecadojogador)):
            if tabuleiro[cash[0]][cash[1]] == Pecadojogador[x]:
                MoverPeca(posicao_inicial,posicao_final)
                jogador = False
                break
        else:

            if tabuleiro2[cash[0]][cash[1]] == '-':
                print("Você deve escolher uma peça para jogar!")
            else:
                print("Você só pode jogar com suas peças!")
    else:
        print("Jogador 2")
        posicao_inicial = input("digite a posição para selecionar  a ab peça: ")
        posicao_final= input('Digite a posicao para mover a peça: ')
        cash = posicao_inicial
        cash = PosicaoInicial(cash)
        for x in  range(len(Pecadojogador1)):
            if tabuleiro[cash[0]][cash[1]] == Pecadojogador1[x]:
                MoverPeca(posicao_inicial,posicao_final)
                jogador = True
                break
        else:

            if tabuleiro2[cash[0]][cash[1]] == '-':
                print("Você deve escolher uma peça para jogar!")
            else:
                print("Você só pode jogar com suas peças!")
        



    
    

   
   