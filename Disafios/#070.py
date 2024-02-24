print('='*30)
print('MERCADÃO DO JEFÃO')
print('='*30)
print('~'*30)
maisde1000 = 0
total = 0
while True:
    nome = input('Produto: ')
    preco = float(input('Preço: R$'))
    escolha = input('Quer continuar? [S|N]').upper()
    print('-'*30)
    print('~'*30)
    
    if preco > 1000.0:
        maisde1000 += 1
    total += preco
    if escolha == 'N':
        break
print(f'A quantidade de produtos que custam mais de 1000 R$ é {maisde1000}')
print(f'A soma de todos os preços é de {total} R$')