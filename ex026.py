frase = str(input('Digite aqui sua frase: ')).upper().strip()
print('A sua frase possuí cerca de {} letras A´s'.format(frase.count('A')))
print('A sua primeira letra A da frase se encontra na posição {}'.format(frase.find('A') + 1))
print('A sua última letra A da frase se encontra na posição{}'.format(frase.rfind(('A') + 1)))