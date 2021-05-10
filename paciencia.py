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