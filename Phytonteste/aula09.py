# Manipulando Texto

frase ='Curso em video Python'
print(frase[::2])

#Escrevendo texto inteiro coloca 3 " no começo e no fim para que apareça o text.

print("""Olá esse é um exemplo de como fazer com que apareça um texto inteiro
com isso, pode ser feito um texto sem que corte ou coloque print eno começo de todas as frases
evitando assim comandos desnecessarios.""")

print(frase.count('o'))
print(frase.upper())
print(len(frase))
print(len(frase.strip()))
frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
dividido = frase.split()
print(dividido)
