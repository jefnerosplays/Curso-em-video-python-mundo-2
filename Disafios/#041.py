n = int(input('Que ano vc nascimeto? '))
i = 2024
h= i - n
print('O atleta tem {} anos'.format(h))
if h <= 9:
    print('O atleta é MIRIM')
elif h <= 9 :
    print('O atleta é INFANTIL')
elif h <= 14:
    print('O atleta é JUNIOR')
elif h <= 19:
    print('O atleta é SÊNIOR')
elif h <= 25:
    print('O atleta é MASTER')
