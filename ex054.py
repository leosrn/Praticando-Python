from datetime import date
na = 0
ja = 0
for n in range (1,8):
    idade = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(n)))
    if date.today().year - idade < 18:
        na = na + 1
    else:
        ja = ja + 1

print('Temos {} pessoas menores de idade e {} pessoas maiores de idade.'.format(na,ja))