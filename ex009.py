#Crie um programa que leia uma quanto uma pessoa tem na carteira e mostre quantos Dólares ele pode comprar.
#Dólar dia 02/04/2025 = R$5,68

din = float(input('Digite quanto você deseja converter: '))
dindol = din / 5.68
print('Você tem ${:.2f}' .format(dindol))