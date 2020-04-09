print('Digite os valores dos lados.')
lado1 = float(input('Quanto vale o L1? '))
lado2 = float(input('Quanto vale o L2? '))
lado3 = float(input('Quanto vale o L3? '))
if lado1 < lado2 + lado3 and lado2 < lado3 + lado1 and lado3 < lado1 + lado2:
    print('Os segmentos podem formar um triângulos ', end='')
    if lado1 == lado2 == lado3:
        print('Equilatero')
    elif lado1 != lado2 != lado3 != lado1:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Não podem formar triângulo')