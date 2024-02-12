i = int(input('INICIO: '))
f = int(input('Fim: '))

soma = 0
cont = 0
for c in range (i, f+1, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma =  soma + c
print('Quantidade de números: {}\n Soma dos números: {}'.format(cont, soma))
