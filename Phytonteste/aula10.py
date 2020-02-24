#Se  e Senão  = If e Else
#exemplo: Se carro.siga() = if carro.siga():
#exemplo: Senão carro.siga() = else carro.siga():

tempo = int(input('Quantos anos tem seu carro ?'))
if tempo <=3:
    print('Seu carro é zerado eim !')
else:
    print('Tamo junto parceiro!')
print('--FIM--')
-----------------------------------------------------------
#outra maneira de escrever seria :
# print('Carro novo' if tempo<=3 else 'carro velho')