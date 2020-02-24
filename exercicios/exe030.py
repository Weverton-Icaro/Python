# ESCREVA UM PROGRAMA QUE INFORME SE OO NÚMERO É PAR OU IMPAR

num = int(input('Escreva um número: '))

num2 = num % 2
if num2 == 0:
    print ('O número infomrado é {}, ele é um numéro PAR.'.format(num))

else:
    print('O número informado é {}, ele é um número IMPAR.'.format(num))

