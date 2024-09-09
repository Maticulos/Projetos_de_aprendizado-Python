print('Desafio 12! ')
pp1 = int(input('Digite o preço do produto(R$): '))
d1 = int(input('Digite o valor de seu desconto(%):'))
print('Com seu desconto de {}%, pode levar por apenas R${}!'.format(d1, pp1-(pp1*(d1/100))))