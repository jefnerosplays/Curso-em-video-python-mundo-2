n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('REPROVADO')
elif m == 5.0 or 5.5 or 6.0 or 6.5 or 6.9:
    print('Recuperação')
elif m > 7.0:
    print('APROVADO')

