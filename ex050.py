soma = 0
for n in range(1,7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma = soma + num
print('--==--'*15)
print('A soma dos valores pares dos números inteiros digitados acima é: {}'.format(soma))