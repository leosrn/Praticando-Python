dias = int(input('Por quantos dias o carro foi utilizado? '))
qkm = int(input('Quantos quilômetros foram rodados com o carro? '))
vt = float((dias*60)+(0.15*qkm))
print('O valor total a ser pago pelo carro será de R${:.2f}'.format(vt))