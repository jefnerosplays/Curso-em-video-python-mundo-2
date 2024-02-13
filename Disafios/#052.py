n = int(input('Digite um número: '))
h = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end= ' ')
        h = h +1
    else:
        print('\033[31m', end = ' ')
    print('{}'.format (c), end='')
print('\n\033[mO numero  {} foi divisivel {} vezes'.format(n, h))
if h > 2:
    print('Portanto não é primo')
else:
    print('O número é primo')


