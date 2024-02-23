n = 0
s = 0
q = 0
while n != 999:
    n = int(input('Digite um valor: '))
    
    if n == 999:
        break
    s += n
    q += 1
print(f'Vc digitou {q} algarismos, e a soma deu {s}')