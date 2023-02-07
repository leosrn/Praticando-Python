vat = float(input('Qual a velocidade atual do carro? '))

if vat>80:
    print('MULTADO! Você excedeu o limite que é de 80Km/h\n Você deve pagar uma multa de R${:.2f}'.format((vat-80)*7))
else:
    print('Obrigado pela colaboração, sua segurança também é a nossa!')