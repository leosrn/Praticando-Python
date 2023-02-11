n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
resp = 0
while resp != 5:
    resp = int(input('[ 1 ] soma\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nOpção: '))
    if resp == 1:
        print('A soma entre {} e {} resulta em {}.'.format(n1, n2, n1 + n2))
        print('--==--'*10)
    elif resp == 2:
        print('A multiplicação entre {} e {} resulta em {}.'.format(n1, n2, n1 * n2))
        print('--==--' * 10)
    elif resp == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é o {}.'.format(n1,n2,n1))
            print('--==--' * 10)
        else:
            print('O maior número entre {} e {} é o {}.'.format(n1,n2,n2))
            print('--==--' * 10)
    elif resp == 4:
        print('--==--' * 10)
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif resp == 5:
        print('Fim!')
    else:
        resp = int(input('Opção invalida, digite novamente: '))