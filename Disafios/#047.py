i = int(input('INÍCIO: '))
f = int(input('FIM: '))

for c in range(i, f+1):
    if c % 2 == 0:
        print(c)