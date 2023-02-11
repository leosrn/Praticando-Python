maior = hom = mul = tot = 0
resp = 'S'
while resp == 'S':
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper().strip()
    resp = str(input('Deseja continuar[S/N]? ')).upper().strip()
    tot += 1
    print('--==--'*10)
    if idade >= 18:
        maior += 1
    elif sexo == 'M':
        hom += 1
    elif sexo == 'F' and idade < 20:
        mul +=1

    if resp == 'N':
        break
    elif resp != 'N' and resp != 'S':
        print('Opção inválida, digite novamente!')
        resp = str(input('Deseja continuar[S/N]? ')).upper().strip()

print(f'Foram cadastradas {tot} pessoas sendo {maior} maior de idade, um total de {hom} homens e um total de {mul} mulheres abaixo de 20 anos!')
print('Programa finalzado!')
