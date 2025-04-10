#Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

val = float(input('Digite o valor do produto que deseja saber o desconto: '))
desc = float(input('Digite o valor do desconto: '))
valdesc = val * (desc / 100)
valfinal = val - desc
print('O desconto ficou no total R${:.2f} e o valor do produto ficará R${:.2f}' .format(valdesc, valfinal))