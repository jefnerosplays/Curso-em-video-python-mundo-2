j = int(input('Que ano vc nasseu : '))
i = 2024 - j
k= i - 18
if i < 18:
    print('Vc ainda vai se alistar no serviço militar, ainda faltam {} anos'.format(i))
elif i == 18:
    print('Já é hora de se alistar no serviço militar.')
elif i > 18:
    print('Já se passou a hora de alistar para serviço militar, vc deveria ter se alistado a {} anos'.format(k))
