print('='*30)
print('{: ^30}'.format('BANCO J.E.F'))
print('='*30)
valor = float(input('Quanto vc quer sacar? R$'))
total = valor
ced = 50
totced =0
while True:
    if valor >= ced:
         total -= ced
         totced += 1
    else:
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced == 10
        elif ced == 10:
            ced == 1
        print(f'Total de {totced} cédulas de R${ced}')
        totced = 0
        elif total == 0:
            break