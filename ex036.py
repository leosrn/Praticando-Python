val = float(input('Qual o valor do imóvel? '))
sal = float(input('Qual o salário do comprador? '))
fin = int(input('Em quantos anos deseja simular o financiamento? '))
mes = fin * 12
por = (30 * sal)/100

if val/mes > por:
    print('Seu empréstimo foi negado devido ao valor das parcelas do parcelamento do imóvel ser superior a 30% de seu salário!')
else:
    print('Parabéns, o seu empréstimo no valor de R${:.2f} foi liberado. \nSuas parcelas seram de R${:.2f} durante {} anos.'.format(val,val/mes,fin))

