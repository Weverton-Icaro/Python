import math
n1 = float(input('Informe o valor do cateto oposto: '))
n2 = float(input('Informe o valor do cateto adjacente: '))
hi = math.hypot(n1, n2)
print('A hipotenusa equivale à {:.2f}'.format(hi))
