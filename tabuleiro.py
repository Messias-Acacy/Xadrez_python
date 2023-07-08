tabuleiro = [
   ["T", "C", "B", "R", "D", "B", "C", "T"],
   ["P", "P", "P", "P", "P", "P", "P", "P"],
   ["-", "-", "-", "-", "-", "-", "-", "-"],
   ["-", "-", "-", "-", "-", "-", "-", "-"],
   ["-", "-", "-", "-", "-", "-", "-", "-"],
   ["-", "-", "-", "-", "-", "-", "-", "-"],
   ["p", "p", "p", "p", "p", "p", "p", "p"],
   ["t", "c", "b", "r", "d", "b", "c", "t"]
]
def tabuleiro_jogo():
   contador = 9
   posicao_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
   linha = ['|', '|', '|', '|', '|', '|', '|', '|']
   horinzontal = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_","_", "_"]
   print()
   for x in range(len(tabuleiro)):
       contador = contador - 1
       print(contador, end=' ')
       print(linha[x], end='  ')
       for y in range(len(tabuleiro)):
           print(tabuleiro[x][y], end='  ')
       print()

   print("   ", end='  ')

   for z0 in range(len(horinzontal)):
       print(horinzontal[z0], end='')
   
   print()
   print("   ", end='  ')
   
   for z in range(len(posicao_letras)):
       print(posicao_letras[z], end='  ')
   return ''


print(tabuleiro_jogo())


