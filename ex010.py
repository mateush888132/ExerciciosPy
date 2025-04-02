#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área  e a quantidade de tinta necessária para pinta-lás, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))

area = altura * largura
litros = area / 2

print('Para pintar sua parede com área de {} são necessários {}L de tinta' .format(area, litros))