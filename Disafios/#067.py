n = 0
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    for c in range (1, 11):
        i = n *  c
        print(f'{n} X {c} = {i}')
    
if n <0:
    print('!!!Não é possovel calcular a tabuada de um número negativo')
else:
    print('')