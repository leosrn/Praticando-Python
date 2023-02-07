import random
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-=-'*20)
chut = int(input('Em que número eu pensei? '))

adv = random.randint(0,5)

if chut == adv:
    print('Parabéns!Você conseguiu me vencer')
else:
    print('Ganhei! Eu pensei no número {} e não no {}...'.format(adv,chut))
