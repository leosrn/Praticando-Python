t1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = t1 + (10 - 1) * r
for c in range(t1,d + r,r):
    print(c, '->', end=' ')

print('Acabou', end=' ')