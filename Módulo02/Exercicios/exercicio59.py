'''Crie um programa que leia dois valores e mostre um menor na tela:
"[1]somar"
"[2]multiplicar"
"[3]maior"
"[4]novos números"
"[5]sair do programa"

Seu programa deverá realizar a operação solicitanda em cada caso.'''

print('Informe dois valores!')
numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))
opção = 0
soma = 0
multi = 0
maior = 0
while opção != 5 :
  opção = int(input('''Selecione uma das alternativas:
  =-=-=-=-=-=-=-=-=-=-=
  "\033[0;30;41m[1]\033[m somar"
  "\033[0;30;41m[2]\033[m multiplicar"
  "\033[0;30;41m[3]\033[m maior"
  "\033[0;30;41m[4]\033[m novos números"
  "\033[0;30;41m[5]\033[m sair do programa"
  =-=-=-=-=-=-=-=-=-=-=
  ------->: '''))
  if opção == 1:
    soma = numero1 + numero2
    print('A soma dos números {} e {} é {}.'.format(numero1, numero2, soma))
  elif opção == 2:
    multi = numero1 * numero2
    print('A multiplicação dos números {} e {} é {}.'.format(numero1, numero2, multi))
  elif opção == 3:
    if numero1 > numero2:
      print('O número maior é {}.'.format(numero1))
    else:
      print('O número maior é {}.'.format(numero2))
  elif opção == 4:
    numero1 = int(input('Primeiro valor: '))
    numero2 = int(input('Segundo valor: '))
print('FIM')