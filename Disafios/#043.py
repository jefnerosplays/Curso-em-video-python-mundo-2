p = float(input('Quanto vc peso? KG '))
alt = float(input('Qual é a sua altura? m '))
imc = p / (alt**2)
if imc  < 18.5:
    print('-Abaixo do peso')
elif imc  >= 18.5 < 25.0:
     print('-Peso ideal')
elif imc  >= 25.0 <30.0:
     print('-Sobrepeso')
elif imc  >= 30.0 < 40.0:
    print('-Obesidade')
elif imc > 40.0:
    print('-Obesidade mórbida')

print('Seu indice de massa corpória é de {:.1f}'.format(imc))