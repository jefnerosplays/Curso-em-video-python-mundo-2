n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]'))
    soma += n
    cont += 1
print('Vc digitou {} algarismos, a soma deles equivale a {}'.format(cont - 1, soma - 999))