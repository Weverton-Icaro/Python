n1 = int(input('Qual a largura da parede? '))
n2 = int(input('Qual a altura da parede ? '))
a = n1 * n2
a2 = a ** 2
print('A parede tem {}m2'.format(a2))
s = a2 / 2
print('Será preciso {}L de tinta'.format(s))