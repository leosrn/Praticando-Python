num = int(input('Digite um número inteiro: '))
tot = 0
for n in range(1,num + 1):
    if num % n == 0:
        print('\033[34m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')

    print('{}'.format(n), end='')

print('\n\033[mO número {} foi dividido {} vezes.'.format(num,tot), end=' ')
if tot == 2:
    print('E ele é Primo!'. format(num))
else:
    print('E ele não é Primo!'. format(num))
