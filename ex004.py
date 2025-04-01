#Faça um programa que leia um número inteiro e mostre o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print('Seu número {} tem como sucessor {} e antecessor {}' .format(n, s, a))