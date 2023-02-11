from random import randint
palp = 0
print('''Sou seu computador e acabei de pensar em um número inteiro entre 0 e 10.
Será que você consegue advinhar qual foi?''')
comp = randint(0,10)
num = int(input('Qual o seu palpite? '))
while num != comp:
    num = int(input('Palpite incorreto! Tente novamente: '))
    if num < comp:
        print('Mais... Continue tentando!')
    else:
        print('Menos... Continue tentando!')
    palp += 1
print('--==--'*15)
print('Parabéns eu pensei no número {} e você acertou com {} tentativas.'.format(comp,palp))

