import random
al1 = str(input('1° aluno: '))
al2 = str(input('2° aluno: '))
al3 = str(input('3° aluno: '))
al4 = str(input('4° aluno: '))
alunos = [al1, al2, al3, al4]
print('O auno escolhido para apagar o quadro foi o {}!'.format(random.choice(alunos)))