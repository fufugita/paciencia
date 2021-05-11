def cria_baralho():
    baralho = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "Q♠", "J♠", "K♠", "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "Q♥", "J♥", "K♥", "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "Q♦", "J♦", "K♦", "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "Q♣", "J♣", "K♣"]

    return baralho

def extrai_naipe(carta):
    for i in carta:
        if i == '♠' or i == '♥' or i == '♦' or i == '♣':
            return i

def extrai_valor(valor):
    for j in valor:
        if j == 'A' or j =='Q' or j == 'J' or j == 'K':
            return j
        elif j == '2' or j == '3' or j == '4' or j == '5' or j =='6' or j == '7' or j == '8' or j == '9':
            return j
        elif j == '1':
            return '10'

def lista_movimentos_possiveis(b, i):
    final = []

    if i == 0:
        return final

    for j in b[i]:
        print(j)

        if j == '1' or j == '2':
            j = '10'
      
            if  j == extrai_valor(b[i-1]) or j == extrai_naipe(b[i-1]):
                final.append(1)

            if i >= 3:
                if j == extrai_naipe(b[i-3]) or j == extrai_valor(b[i-3]):
                     final.append(3)

        else:   
            if  j == extrai_valor(b[i-1]) or j == extrai_naipe(b[i-1]):
                final.append(1)

            if i >= 3:
                if j == extrai_naipe(b[i-3]) or j == extrai_valor(b[i-3]):
                    final.append(3)

            
    return final

def empilha(baralho, origem, destino):

    carta = baralho[origem]
    baralho.remove(baralho[origem])
    baralho[destino] = carta
    
        
    return baralho

def possui_movimentos_possiveis(lista):

    soma = 0

    for i in range(len(lista)):
        x = lista_movimentos_possiveis(lista, i)    
        if x != []:
            soma += 1
    if soma > 0:
        return True
    else:
        return False

def cores(n):
    if extrai_naipe(n) == '♠':
        c= f'\033[1;34;40m{n}\033[0m'
    if extrai_naipe(n) == '♥':
        c= f'\033[1;31;40m{n}\033[0m'
    if extrai_naipe(n) == '♣':
        c= f'\033[1;32;40m{n}\033[0m'
    if extrai_naipe(n) == '♦':
        c= f'\033[1;35;40m{n}\033[0m'
    return c