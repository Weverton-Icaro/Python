num1 = int(input('Informe um número:'))
num2 = int(input('Informe outro número: '))
num3 = int(input('Informe mais um número:'))

if num1 > num2 and num2 > num3:
    print('O número maior é {}'.format(num1))
    print('O menor número é {}'.format(num3))
if num1 < num2 and num2 < num3:
    print(' O número maior é {}'.format(num3))
    print(' O número menor é {}'.format(num1))
if num1 < num2 and num1 > num3:
    print('O número maior é {}'.format(num2))
    print(' O número menor é {}'.format(num3))


print('--FIM--')