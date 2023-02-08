from datetime import date
ano = int(input('Digite aqui seu ano de nascimento: '))
idade = date.today().year - ano
print('Pessoas nascidas no ano de {} completam {} anos no ano de {}'.format(ano,idade,date.today().year))

if idade < 18:
    print('Portanto, ela deverá se alistar apenas daqui {} ano(s) no ano de {}'.format(18 - idade,(18 - idade)+date.today().year))
elif idade > 18:
    print('Portanto, ela ja deveria ter se alistado em {} à {} ano(s) atrás!'.format(ano + 18,date.today().year - (ano + 18)))
elif idade == 18:
    print('Você deve se alistar imediatamente!')


