n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1 + n2) / 2
print('A média total do aluno foi de: {:.1f}'.format(med))

if med < 5.0:
    print('O aluno está reprovado!')
elif med >= 5.0 and med <= 6.9:
    print('O aluno está de recuperação')
elif med >= 7.0:
    print('Parabéns! O aluno está aprovado.')