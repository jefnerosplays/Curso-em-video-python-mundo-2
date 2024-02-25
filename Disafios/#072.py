t = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez')
n = int(input('Digite um número entre 1 e 10: '))
l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    if n in l:
        print(t[n])
        break
    else:
        print('Tente novamente')
        n = int(input('Digite um número entre 1 e 10: '))