nome = str(input('Qual o nome do funcionário? '))
val = float(input('Qual o salário do funcionário? '))
aum = float(input('Qual porcentagem deseja dar de aumento? '))
v1 = aum*val
v2 = v1/100
vt = val+v2
print('O funcionário {} terá um aumento de {}% num total de R${:.2f} que fará com que seu salário passe de R${:.2f} para R${:.2f} .'.format(nome,aum,v2,val,vt))