rank = 'Python','C','C++','Java','C#','Visual Basic','Javascript'
posi =rank.index('Python') + 1
print('='*50)
print('{: ^50}'.format('RANKING DAS LINGUAGENS MAIS USADAS'))
print('='*50)
print(f'Os cinco primeiros no rank são{rank[0: 5]}')
print('='*70)
print(f'Os quatro ultimos no rank são{rank[-4: 7]}')
print('='*80)
print(f'Em ordem alfabetica{sorted(rank)}')
print('='*90)
print(f'-->O python está na poisição {posi}°')