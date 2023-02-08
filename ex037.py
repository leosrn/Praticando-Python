num = int(input('Escreva um número inteiro qualquer: '))
esc = int(input('Escolha o metodo de conversão: \n[1]Binário\n[2]Octal\n[3]Hexadecimal\ndigite aqui: '))

if esc == 1:
    print('O número {} convertido para Binário é igual a: {}'.format(num,bin(num)[2:]))
elif esc == 2:
    print('O número {} convertido para Octal é igual a: {}'.format(num,oct(num)[2:]))
elif esc == 3:
    print('O número {} convertido para Hexadecimal é igual a: {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida!')