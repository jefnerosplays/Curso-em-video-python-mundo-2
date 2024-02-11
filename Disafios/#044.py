p = float(input('Quanto custa o produto?: '))
c = input('Qual é a condição de págamento?\n[1]Á vista dinheiro/cheque\n[2]Á vista no cartão\n[3]Em até 2x no cartão\n[4]3x ou mais no cartão\n->')
if c == '1':
    j= p * (10/100)
    print('O valor ficou de {}R$ com desconto de 10%'.format(j))
elif c =='2':
    j= p * (5/100)
    print('O valor ficou de {}R$ com desconto de 5%'.format(j))
elif c == '3':
    print('O valor ficou de {}R$ sem deconto'.format(p))
elif c == '4':
    j= p * (20/100)
    k= p + j
    print('O valor ficou de {}R$ com 20% de juros')


