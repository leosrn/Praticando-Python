dist = float(input('Qual será a distância da sua viagem? '))
if dist<200:
    print('Você está prestes a começar uma viagem de {:.1f}Km.\n E o preço da sua passagem será de R${:.2f}'.format(dist,dist*0.50))
else:
    print('Você está prestes a começar uma viagem de {:.1f}Km.\n E o preço da sua passagem será de R${:.2f}'.format(dist,dist*0.45))
