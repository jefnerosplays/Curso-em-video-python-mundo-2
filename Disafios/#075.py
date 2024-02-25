n = int(input('Digite um número: '))
g = int(input('Digite outro número: '))
h = int(input('Digite mais um número: '))
k = int(input('Digite outro: '))
culp = (n,g,h,k)
par = 0
quant9 = culp.cont(9)
posi =culp.index(3) + 1
for c in culp:
    if c % 2 ==0:
        par += 1
print(f'Vc digitou os números {culp}')
print(f'O valor 9 aparesceu {quant9} vezes')
print(f'O valor 3 aparesceu na posição{posi}')
print(f'Tem {par} numeros pares no total')