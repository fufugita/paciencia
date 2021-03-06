from paciencia import *
from random import shuffle

print(  '''
    Paciência Acordeão 
    ================== 
    Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. 
    Existem apenas dois movimentos possíveis: 
    1. Empilhar uma carta sobre a carta imediatamente anterior; 
    2. Empilhar uma carta sobre a terceira carta anterior. 
    Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: 
    1. As duas cartas possuem o mesmo valor ou 
    2. As duas cartas possuem o mesmo naipe. 
    Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. 
    Aperte [Enter] para iniciar o jogo... 
        '''
)
 
input()

baralho = cria_baralho()

shuffle(baralho)

if possui_movimentos_possiveis(baralho) == False:

    print('Perdeu o Jogo, Não tem mais movimentos possíveis!')

