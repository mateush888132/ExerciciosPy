#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porçao inteira.

import math
from math import trunc

num = float(input('Digite um valor: '))

print('O valor digitado foi {} e sua porção inteira é {} ' .format(num, trunc(num)))
