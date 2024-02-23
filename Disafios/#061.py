print('Gerador de PA')
print('-='*10)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
for c in range (1, n + 1, r):
    print(c,end=' ')