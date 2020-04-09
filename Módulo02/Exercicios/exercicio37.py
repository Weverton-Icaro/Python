num = int(input('Digite um número: '))
print('''Escolha um para as bases de conversão: 
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
op = int(input('Qual será? '))
if(op) == 1:
    print(bin(num)[2:])
elif(op) == 2:
    print(oct(num)[2:])
elif(op) == 3:
    print(hex(num)[2:])
else:
    print('Opção invalida!')