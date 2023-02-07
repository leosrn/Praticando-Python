nome = str(input('Digite aqui seu nome completo: ')).strip()
snome = nome.split()
print('Seu primeiro nome é: {}'.format(snome[0].capitalize()))
print('Seu último nome é: {}'.format(snome[len(snome)-1].capitalize()))




