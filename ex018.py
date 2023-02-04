import math
from math import asin, atan, acos
grau = int(input('Escreva o grau que deseja calcular: '))
sen = math.sin(math.radians(grau))
cos = math.cos(math.radians(grau))
tan = math.tan(math.radians(grau))
print('O seno do Ângulo de {}° é: {:.3f}'.format(grau,sen))
print('O cosseno do Ângulo de {}° é: {:.3f}'.format(grau,cos))
print('A tangente do Ângulo de {}° é: {:.3f}'.format(grau,tan))