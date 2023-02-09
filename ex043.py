peso = float(input('Peso(kg): '))
alt = float(input('Altura(m):'))
imc = peso / (alt**2)

print('Seu IMC é de {:.1f}.'.format(imc))

if imc <= 18.5:
    print('Status: Abaixo do Peso.')
elif imc <= 25:
    print('Status: Peso ideal.')
elif imc <= 30:
    print('Status: Sobrepeso.')
elif imc <= 40:
    print('Status: Obesidade Mórbida.')


