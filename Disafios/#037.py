j = int(input('Digite o numero que vc quer converter a base: '))
h = int(input('Escolha a base:\n[1]Binário\n[2]Octal\n[3]Hexadecimal\n-->'))
if h == '1':
    print(bin(j)[2:])
elif h == '2':
    print(oct(j)[2:])
elif h == '3':
    print(hex(j)[2:])