num = int(input('Digite um número: '))
resp = str(input('Deseja continuar [S/N]? ')).upper().strip()
c = 1
soma = 0
maior = 0
menor = num
while resp == 'S':
    c += 1
    soma += num

    if num > maior:
        maior = num
    elif num > menor:
        menor = num

    num = int(input('Digite um número: '))
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()

    if resp not in 'SsNn':
        print('Opção inválida, digite novamente!')
        resp = str(input('Deseja continuar [S/N]? ')).upper().strip()
print('Você digitou {} números e a média entre eles foi de {}.'.format(c, soma/c))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))