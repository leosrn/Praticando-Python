mul = 0
id = 0
mv = 'Ninguém'
cid = 0
for n in range(1,5):
    print('----- {}ª Pessoa -----'.format(n))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    cid = idade + cid
    if sexo == 'M' and idade > id:
        mv = nome
        id = idade
    elif sexo == 'F' and idade < 20:
        mul = mul + 1
media = int(cid / 4)
print('A média de idade foi de {} anos.'.format(media))
print('Foram registradas {} mulheres abaixo de 20 anos.'.format(mul))
print('O homem mais velho foi o {}'.format(mv))