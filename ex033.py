a = int(input('Digite o primeiro número inteiro: '))
b = int(input('Digite o segundo número inteiro: '))
c = int(input('Digite o terceiro número inteiro: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))
