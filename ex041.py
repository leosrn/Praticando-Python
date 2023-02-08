from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('A categoria do atleta é a Mirim.')
elif idade <= 14:
    print('A categoria do atleta é a Infantil.')
elif idade <= 19:
    print('A categoria do atleta é a Júnior.')
elif idade <= 25:
    print('A categoria do atleta é a Sênior.')
else:
    print('A categoria do atleta é a Master.')