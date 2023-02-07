sal = float(input('Qual o seu salário? R$'))
if sal <= 1250.00:
    aum = (sal * 15) / 100
    print('O seu salário atual será de R${:.2f} com um aumento de R${:.2f}!'.format(sal+aum,aum))
else:
    aum = (sal * 10) / 100
    print('O seu salário atual será de R${:.2f} com um aumento de R${:.2f}!'.format(sal+aum,aum))