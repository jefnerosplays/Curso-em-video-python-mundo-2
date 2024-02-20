n1 = int(input('Escolha o primeiro número: '))
n2 = int(input('Escolha o segundo número: '))
l = 0
while l != 5:
    l = int(input('[1] somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\n>>>>>Qual é a sua opção?'))
    if l == 1:
        s = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, s))
    elif l == 2:
        s = n1 * n2
        print('A multiplicação {} * {} = {}'.format(n1, n2 , s))
    elif l == 3:
        if n1 > n2:
            print('O maior é {}'.format(n1))
        elif n2 > n1:
            print('O maior número é {}'.format(n2))
    elif l == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif l == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
print('Fim')