import random
i = ('Pedra','Papel','Tesoura')
comp =random.randint(0, 2)
print('Suas opções:\n[ 0 ]PEDRA\n[ 1 ]PAPEL\n[ 2 ]TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('-='*20)
print('Computador jogou {}'.format(i[comp]))
print('Jogador jogou {}'.format(i[jogador]))
print('-='*20)
if comp == 0:
    if  jogador == 0:
        print('->IMPATE')
    elif jogador == 1:
        print('->VITÓRIA')
    elif jogador == 2:
        print('->DERROTA')
    else:
        print('->Jogada inválida')
if comp == 1:
    if jogador == 0:
        print('->DERROTA')
    elif jogador == 1:
        print('->IMPATE')
    elif jogador == 2:
        print('->VITÓRIA')
    else :
        print('->Jogada inválida')
if comp == 2:
    if jogador == 0:
        print('->VITÓRIA')
    elif jogador == 1:
        print('->DERROTA')
    elif jogador == 2:
        print('->IMPATE')
    else:
        print ('Jogada inválida')