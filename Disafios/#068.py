from random import randint
print('='*80)
print('VAMOS JOGAR PAR OU IMPAR?')
print('='*80)
jogador = int(input('Escolha uma oção:\n[1]Impar\n[2]Par\nSua escolha -> '))
jogadornum = int(input('>|Numero do jogador : '))
computadornum = randint(1, 10)
print(f'>|Número do computador : {computadornum}')
soma = jogadornum + computadornum
if jogador == 1:
    computador = int(2)
    if soma % 2 != 0:
        print(f'Vc ganhou!! {jogadornum} + {computadornum} equivale a um numero impar ({soma}) e o computador escolheu par!!')
    if soma % 2 == 0: 
        print(f'Vc perdeu!! {jogadornum} + {computadornum} equivale a um numero par ({soma}) e o jogador escolheu impar!!')
if jogador == 2:
     computador = int(1)
     if soma % 2 != 0:
        print(f'Vc perdeu!! {jogadornum} + {computadornum} equivale a um numero impar ({soma}) e o jogador escolheu par!!')
     if soma % 2 == 0:
         print(f'Vc ganhou!! {jogadornum} + {computadornum} equivale a um numero par ({soma}) e o computador escolheu impar!!')
print('='*80)