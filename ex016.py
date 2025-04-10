#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

cat = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateto adjacente: '))
hipo = math.hypot(cat, adj)
print('A hipotenusa vai medir {:.2f}' .format(hipo))
