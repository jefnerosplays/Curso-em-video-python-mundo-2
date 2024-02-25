from random import randint
c = (randint(1, 11),randint(1,11),randint(1,11),randint(1,11),randint(1, 11))
print('Os valores sortiados foram:')
for n in c:
    print(f' {n} ' , end = '')
print(f'\nO maior valor sorteado foi {max(c)}')
print(f'O menor valor sorteado foi {min(c)}')