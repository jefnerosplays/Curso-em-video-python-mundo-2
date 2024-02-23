num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma += num
    cont += 1
print('Vc digitou {} números.'.format(cont - 1))
print('A soma dos algarismos é {}'.format(soma - 999))
