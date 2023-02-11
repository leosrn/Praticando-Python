import math
c = 0
num = int(input('Digite um número inteiro: '))
r = int(input('Digite a razão da progressão: '))
while c < 10:
    print('{} -> '.format(num), end='')
    num += r
    c += 1
print('FIM!')
