n = 0
soma = 0
média = 0
maior idade = 0
nome mais velho = 0
for c in range(4):
    n += 1
    print('------{}°PESSOA-----'.format(n))
    N = input('NOME: ')
    I = int(input('IDADE: '))
    S = input('SEXO [M\F]: ')
    soma += I
print('-'*18)
if c == 1:
    maior idade = idade
    nome mais velho = nome
    média = soma /4
    print('A média de idade do grupo é de {} anos'.format(média))