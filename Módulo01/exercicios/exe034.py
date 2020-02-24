salario = int(input('Qual o seu o valor do seu salário?'))

if salario >= 1250:
    aumento1 = (salario * 10) / 100
    result1 = aumento1 + salario
    print(' O aumento do seu salário será de R${:2}'.format(aumento1))
    print(' Seu soldo será de R${:2}'.format(result1))
else:
    aumento2 =  (salario * 15) /100
    result2 = salario + aumento2
    print(' O aumento do seu salário será de R${:2}'.format(aumento2))
    print(' Seu soldo será de R${:2}'.format(result2))

print('--fim--')


