print('     Tabuada 2.0')
print('-='*10)
n = int(input('Digite um número para ver a tabuada do mesmo: '))
for c in range (1, 11):
    i =n * c
    print(' {} x {} = {}'.format(n, c, i))
