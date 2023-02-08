a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

if a == b:
    print('Os valores {} e {} são iguais!'.format(a,b))
elif a < b:
    print('O segundo valor({}) é o maior!'.format(b))
elif a > b:
    print('O primeiro valor({}) é o maior!'.format(a))