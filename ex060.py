from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = factorial(num)

while c > 0:
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    c -= 1

print(f , end='')


