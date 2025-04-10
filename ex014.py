#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60,00 por dia e R$0,15 por Km rodado.

dias = float(input('Digite a quantidade de dias com o carro: '))
km = float(input('Digite a quantidade de KM rodado com o carro: '))
valdias = 60 * dias
valkm = 0.15 * km
valfinal = valdias + valkm
print('Você alugou o carro por {} dias' .format(dias))
print('Você dirigiu por {} KM' .format(km))
print('Resultando em R${:.2f} pelos dias e R${:.2f} pelos Km' .format(valdias, valkm))
print('O total será de R${:.2f}' .format(valfinal))