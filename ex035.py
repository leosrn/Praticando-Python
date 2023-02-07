r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))
if r1<r2 + r3 and r2<r1 + r3 and r3<r1 + r3:
    print('Com esses valores é possível se obter um triângulo!')
else:
    print('Com esses valores não é possível se obter um triângulo!')

