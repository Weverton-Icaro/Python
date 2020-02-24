algo = input('Digite algo:')
print('Qual é o tipo primitivo desse valor?', type(algo))
print('É composto por números ?', algo.isnumeric())
print('É composto por letras?', algo.isalpha())
print('É composto por letras e números?', algo.isalnum())
print('É compsoto por letras maiusculas?', algo.isupper())
print('É composto por letras minusculas?', algo.islower())
print('É composto por espaços?', algo.isspace())

