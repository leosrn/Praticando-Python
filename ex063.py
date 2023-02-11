termo = int(input('Quantos termos deseja mostrar? '))
num1 = 0
num2 = 1
num3 = num1 + num2
numx = 0
c = 3
print('{} -> {}'.format(num1, num2, ), end='')
while c <= termo:
    num3 = num1 + num2
    print(' -> {}'.format(num3), end='')
    num1 = num2
    num2 = num3
    c += 1
print(' -> FIM', end='')

