q = 0
c = 0
maisde18 = 0
menosde20 = 0
homems = 0
while c == 0:
    sexo = input('Qual é seu genero? [M|F]: ').upper()
    idade = int(input('Qual é a sua idade? '))
    n = input('Quer continuar? [S|N]: ').upper()
    print('~'*30)
    if n == 'N':
        c = 1
    if idade > 18:
        maisde18 = maisde18 + 1
    if sexo == 'M':
        homems += 1
    if sexo == 'F' and idade < 20:
        menosde20 += 1

print(f'->A quantidade de pessoas com mais de 18 anos é {maisde18}')
print(f'->Foram registrados {homems} homens')
print(f'->Foram registradas {menosde20} mulheres com menos de 20 anos')