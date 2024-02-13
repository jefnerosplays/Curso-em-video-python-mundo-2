maior = 0
menor = 0

for c in range(1, 6):
    n = float(input('Qual é o peso da {}° pessoa?: '.format(c)))
    if c == 1:
        maior = c
        menor = c
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print ('{}KG é o maior peso.'.format(maior))
