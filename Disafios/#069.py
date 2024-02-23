q = 0
c = 0
maisde18=0
while c == 0:
    sexo = input('Qual é seu genero? [M|F]: ').upper()
    idade = int(input('Qual é a sua idade? '))
    n = input('Quer continuar? [S|N]: ').upper()
    print('~'*30)
    if n == 'N':
        c = 1
if sexo == 'M'and idade > 18:
    maisde18 += 1
print(maisde18)