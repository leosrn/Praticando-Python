num = int(input('Digite um número[999 para parar]: '))
c = 0
tot = 0
while num != 999:
    c += 1
    tot += num
    num = int(input('Digite um número[999 para parar]: '))

print('O programa foi finalizado com {} npumeros digitados e a soma entre eles resulta em: {}'.format(c, tot))