from math import radians, cos, sin, tan
a = float(input('Informe o ângulo: '))
sen = sin(radians(a))
print('O seno do ângulo informado é {:.2f}'.format(sen))
cos = cos(radians(a))
print('O Coseno do ângulo é {:.2f}'.format(cos))
tan = tan(radians(a))
print('A tangente do ângulo é {:.2f}'.format(tan))

