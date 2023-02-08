r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))
if r1<r2 + r3 and r2<r1 + r3 and r3<r1 + r3:
    print('Com esses valores é possível se obter um triângulo!')
    if r1 == r2 and r1 == r3:
        print('Sendo este triângulo um Equilátero, ou seja, de todos os lados iguais.')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('Sendo este triângulo um Isósceles, ou seja, com apenas dois lados iguais.')
    else:
        print('Sendo este triângulo um Escaleno, ou seja, com todos os lados diferentes.')
else:
    print('Com esses valores não é possível se obter um triângulo!')
