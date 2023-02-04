val = float(input('Qual o valor do produto? '))
por = int(input('Qual a porcentagem que deseja descontar?'))
v1 = por*val
v2 = v1/100
vt = val-v2

print('O produto cujo custa R${:.2f} sofrerá um desconto de R${:.2f}, ficando com um valor total de R${:.2f} .'.format(val,v2,vt))