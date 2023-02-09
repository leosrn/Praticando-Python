val = float(input('Qual o valor do produto? '))
met = int(input('--=--Método de pagamento--=--\nÀ vista dinheiro/cheque [1]\nÀ vista no cartão [2]\nEm até 2x no cartão [3]\n3x ou mais no cartão [4]\nOpção: '))
print('--==--'*15)
if met == 1:
    vt = val * 10 / 100
    print('O valor total será de R${:.2f} tendo 10% de desconto com um total de R${:.2f}.'.format(val - vt, vt))
elif met == 2:
    vt = val * 5 / 100
    print('O valor total será de R${:.2f} tendo 5% de desconto com um total de R${:.2f}.'.format(val - vt, vt))
elif met == 3:
    print('O valor de R${:.2f} não sofrerá alteração!'.format(val))
elif met == 4:
    vt = val * 20 / 100
    print('O valor total será de R${:.2f} tendo 30% de acréscimo com um total de R${:.2f}.'.format(val + vt, vt))
else:
    print('Opção inválida!')
