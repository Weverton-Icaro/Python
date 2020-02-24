print('Informe o valor de 3 retas, e veja se formam um triângulo.')
r1 = int(input('Informe a reta 1:'))
r2 = int(input('Informe a reta 2:'))
r3 = int(input('Informe a reta 3:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Suas retas formam um triângulo!')
else:
    print('Suas retas não formam um triângulo!')

print('FIM')
