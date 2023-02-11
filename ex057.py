sex = str(input('Sexo [M/F]: ')).upper()
while sex not in 'FfMm':
    sex = str(input('Opção inválida, digite novamente o sexo desejado: ')).upper()

if sex == 'M':
    sex ='Masculino'
else:
    sex = 'Feminino'
print('Sexo {} cadastrado com sucesso!'.format(sex))
