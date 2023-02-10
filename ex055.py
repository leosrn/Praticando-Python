maior = 0
menor = 0
for n in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    else:
        menor = peso
print('o maior foi {:.2f} e o menor foi {:.2f}'.format(maior,menor))

