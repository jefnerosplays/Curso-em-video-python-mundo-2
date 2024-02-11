r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r3 +r1 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR um  triângulo {}!')
    if r1 == r2 == r3:
        print('->EQUILÁTERO')
    if r1 != r2!= r3 != r1:
        print('->ESCALENO')
    else: 
        print('ISÓSCELES')


else:
    print('Os seguimentos acima NÃO PODEM FORAMR um triângulo {}!')
