n = 0
es = 'S'
cont = 0
soma = 0
media = 0
maior = 0

while es != 'N' or '':
    n = int(input('Digite um número: '))
    es = input('Quer continuar? [S|N]').upper()
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior = cont
    else:
        if n > maior:
            maior = n
print('->A soma dos algorismos é {} a quantidade de algarismos é de {} a média é de {} e o algarismo maior é  o {}'.format(soma, cont, media, maior))