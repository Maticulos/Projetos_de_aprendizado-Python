print('Desafio 5! ')
n = int(input('Digite um número: '))
print('Seu antecessor é {} e seu sucessor é {}'.format(n-1, n+1))
print('Desafio 6! ')
n1 = int(input('Digite outro número: '))
print('Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format (n1*2, n1*3, n1**0.5))
print('Desafio 7! ')
p1 = float(input('Digite sua 1° nota: '))
p2 = float(input('Digite sua 2° nota: '))
print('Sua média final é {}'.format((p1+p2)/2))
print('Desafio 8! ')
m1 = int(input('Digite uma distãncia(em metros): '))
print('Sua distância em centímetros é {} e em milimetros é {}'.format(m1*100, m1*1000))
print('Desafio 9! ')
n2 = int(input('Digite outro número: '))
print('A tabuada do número é essa: ',
'{} {} {} {}'.format(n2*1, n2*2, n2*3, n2*4),
'{} {} {} {}'.format( n2*5, n2*6, n2*7, n2*8),
'{} {}'.format( n2*9, n2*10))
print('Desafio 10! ')
n3 = int(input('Digite quanto dinheiro voce tem(R$):'))
print('Voce pode comprar cerca de {:.2f} dólares (dados referentes ao dia 06/09/2024)!'.format(n3/5.57))
print('Desafio 11! ')
l1 = int(input('Digite a largura da parede(m²): '))
c1= int(input('Digite a altura da parede(m²): '))
a1 = l1 * c1
print('Sua parede tem {} m² e precisa de {} litros de tinta'.format(a1, a1/2))
print('Desafio 12! ')
pp1 = int(input('Digite o preço do produto(R$): '))
d1 = int(input('Digite o valor de seu desconto(%):'))
print('Com seu desconto de {}%, pode levar por apenas R${}!'.format(d1, pp1-(pp1*(d1/100))))
print('Desafio 13! ')
s1 = int(input('Digite o valor de seu salário(R$): '))
aa1 = int(input('Digite o valor de seu aumento(%): '))
print('Com o aumento de {}%, seu salário vai de {} para {}'.format(aa1,s1,s1+(s1*(aa1/100))))