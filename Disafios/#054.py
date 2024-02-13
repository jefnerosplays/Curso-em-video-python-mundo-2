n= 0
c = 0
for c in range(7):
    n += 1
    a =int(input('O ano de nascimento da {}° pesso é: '.format(n)))
    i = 2024 - a
    if i >= 21:
        print('Maior de idade')
        c += 1
    else:
        print('Menor de idade')
print('-='*25)
print('A quantidade de pessoas maior de idade é de {} pessoas'.format(c))
print('-='*25)
  