from random import randint
vit = 0
while True:
    num = int(input('Digite um valor entre 0 e 10:'))
    pi = str(input('Par ou Ímpar[P/I]: ')).upper().strip()
    comp = randint(0, 10)
    mod = num + comp
    print(f'Você jogou {num} e o computador jogou {comp}')
    print(f'o total de {num} + {comp} = {num + comp} é: Par' if (num + comp) % 2 == 0 else f'o total de {num} + {comp} = {num + comp} é: Ímpar')

    if mod % 2 == 0 and pi == 'P' or mod % 2 == 1 and pi == 'I':
        print('Você venceu o jogo! Vamos jogar novamente...')
        print('--==--'*10)
        vit += 1
    else:
        break
print('--==--'*10)
print('Game over! Você perdeu!')
print(f'Você atingiu {vit} vitórias consecutivas!')

