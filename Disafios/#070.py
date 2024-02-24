print('='*30)
print('MERCADÃO DO JEFÃO')
print('='*30)
print('~'*30)
maisde1000 = 0
total = 0
menor = 0
cont = 0
while True:
    nome = input('Produto: ')
    preco = float(input('Preço: R$'))
    cont += 1
    escolha = input('Quer continuar? [S|N]').upper()
    print('-'*30)

    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
    
    if preco > 1000.0:
        maisde1000 += 1
    total += preco
    if escolha == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'A quantidade de produtos que custam mais de 1000 R$ é {maisde1000}')
print(f'A soma de todos os preços é de R${total} ')
print(f'O produto mais barato custa R${menor:.2f}')