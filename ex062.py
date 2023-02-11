import math
c = 1
num = int(input('Digite um número inteiro: '))
r = int(input('Digite a razão da progressão: '))
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(num), end='')
        num += r
        c += 1
    print('Pausa!')
    mais = int(input('Quantos termos a mais deseja mostrar? '))
print('Progressão finalizada com {} termos mostrados!'.format(total))
print('FIM!')