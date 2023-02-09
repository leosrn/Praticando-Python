from random import randint
itens = ('Pedra','Papel','Tesoura')
print('''Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jog = int(input('Qual será sua jogada? '))
comp = randint(0,2)

print('--==--'*10)
print('Você jogou {}'.format(itens[jog]))
print('O computador jogou {}'.format(itens[comp]))
print('--==--'*10)

if comp == 0:
    if jog == 0:
        print('Vocês empataram!')
    elif jog == 1:
        print('O jogador venceu!')
    elif jog == 2:
        print('O computador venceu!')
elif comp == 1:
    if jog == 0:
        print('O computador venceu!')
    elif jog == 1:
        print('Vocês empataram!!')
    elif jog == 2:
        print('O jogador venceu!')
elif comp == 2:
    if jog == 0:
        print('O jogador venceu!')
    elif jog == 1:
        print('O computador venceu!!')
    elif jog == 2:
        print('Vocês empataram!')
