from tabuleiro import *





#funções do jogo

def PosicaoInicial(posicao_inicial):
    posicao_inicial_numero = posicao_inicial[0]
    posicao_inicial_letra = posicao_inicial[1]

    if posicao_inicial_numero == "0":
        posicao_inicial_numero = 0
    else:
        posicao_inicial_numero = int(posicao_inicial_numero)-1
    
    #tratando letra
    alteracao_letrapornumero_inicial =  ["a","b","c","d","e","f","g","h"]
    for posicao_letra_i in range(len(alteracao_letrapornumero_inicial)):
        if  posicao_inicial_letra == alteracao_letrapornumero_inicial[posicao_letra_i]:
            posicao_inicial_letra = posicao_letra_i
            break
    #return posicao_final_numero, posicao_final_Letra


    #encontrar a posicao certa na vertical
    posicao_inicial_numero = 7-(len(alteracao_letrapornumero_inicial[0:posicao_inicial_numero])-1)-1
    

    if tabuleiro[posicao_inicial_numero][posicao_inicial_letra] != '-':
        posicao0 = (posicao_inicial_numero,posicao_inicial_letra)
        return posicao0
    

#fazer a def de reconhcer a peça e calcular as jogadas

# def MovimentosDisponiveis(posicao_inicial):
#     PosicaoInicial(posicao_inicial)

#     if tabuleiro[posicao_inicial[0]][posicao_inicial[1]] not in :
#         tabuleiro[posicao_inicial[0]][posicao_inicial[2]] = 'OPAA'
        


def PosicaoFinal(posicao_final):
    posicao_final_numero = posicao_final[0]
    posicao_final_Letra = posicao_final[1]

    #tratando numero
    if posicao_final_numero == "0":
        posicao_final_numero = 0
    else:
        posicao_final_numero = int(posicao_final_numero)-1
    
    #tratando letra
    alteracao_letrapornumero =  ["a","b","c","d","e","f","g","h"]
    for posicao_letra in range(len(alteracao_letrapornumero)):
        if  posicao_final_Letra == alteracao_letrapornumero[posicao_letra]:
            posicao_final_Letra = posicao_letra
            break
    #return posicao_final_numero, posicao_final_Letra


    #encontrar a posicao certa na vertical
    posicao_final_numero = 7-(len(alteracao_letrapornumero[0:posicao_final_numero])-1)-1
    posicao1 = (posicao_final_numero,posicao_final_Letra)
    return posicao1




def MoverPeca(posicaoinicial,posicao_final):
    posicaoinicial = PosicaoInicial(posicaoinicial)
    #fazer ele reconhecer qual a peça
    posicao_final = PosicaoFinal(posicao_final)
    #calcular e verificar se a posição final tá dentro do calculo
    #se estive dentro, exeuctar codigo das linhas 69 e 70, se não, n fazer nada!
    tabuleiro[posicao_final[0]][posicao_final[1]] = tabuleiro[posicaoinicial[0]][posicaoinicial[1]]
    tabuleiro[posicaoinicial[0]][posicaoinicial[1]] ='-'
    return ''




# while True:
#    print(tabuleiro_jogo())
#    posicao_inicial = input("digite a posição para selecionar a peça: ")
#    posicao_final= input('Digite a posicao para mover a peça: ')
#    MoverPeca(posicao_inicial,posicao_final)
   


# while True:
#     print(tabuleiro_jogo())
#     posicaoteste = input("digite a posição para selecionar a peça: ")
#     posicaoteste = PosicaoInicial(posicaoteste)
#     print(posicaoteste)
#     tabuleiro[posicaoteste[0]][posicaoteste[1]] ='OK1!'







