casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o valor do seu sálario? '))
tempo = int(input('Em quantos anos pretente quitar o emprestimo ? '))

soma = (salario * 30 ) / 100
soma2 = casa / tempo
print('O valor da prestação ficou em R$ {:.2f}'.format(soma2))

if soma2 <= soma :
  print('O valor do emprestimo foi aprovado!')
else:
  print('O valor do emprestimo foi negado.')