# COLORINDO O PROGRAMA

# Para colorir um programa usa ( \033[ stylo ; texto ; background; m )  sem parenteses

#Exemplo

# Stylo = 0 ( sem estilo ), 1 negrito, 4 sublinhado e 7 negativo (invertido)
# texto = 30 branco, 31 vermelho , 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 azul bebe, 37 cinza.
# background = 40 , 41, 42, 43, 44, 45, 46, 47 ( mesmas cores do texto)

print('\033[7;30mOlá MUNDO\033[m')

a = 3
b = 5
print('Os valores são \033[1;32;45m{}\033[m e \033[1;33;47m{}\033[m!'.format(a, b))