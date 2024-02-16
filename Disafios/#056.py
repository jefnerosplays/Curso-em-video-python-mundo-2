soma = 0
média = 0
nome = 0
maioridade = 0

for c in range(4):
    print('----- {}° PESSOA -----'.format(c))
    nome = input('NOME: ')
    idade = int(input('IDADE: '))
    sexo = input('SEXO [M|F]: ').upper()
    soma += idade
    if c == 1 and sexo == 'M':
        maioridade = idade
        nome = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade


média = soma / 4
print('A média de idade é de {}'.format(média))
