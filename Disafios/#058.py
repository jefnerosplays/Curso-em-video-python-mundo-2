import random
n = int(input('Tente adivinhar o número que estou pensando entre 1 e 8... '))
c = random.randint(1 , 8)
while n != c:
    n = int(input('Vc errou, tente adivinhar denovo... '))
print('-Vc acertou!!')
print('O numero era {}'.format(c))