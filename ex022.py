nome = str(input('Escreva aqui seu nome completo: ')).strip()
print('Seu nome em maiúsculo: {}'.format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


