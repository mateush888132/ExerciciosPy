#Crie um algorirmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

dob = n * 2
tri = n * 3
raiz = n ** (1/2)
print('O dobro de {} é {}'.format(n, dob))
print('O triplo de {} é {}' .format(n, tri))
print('A raiz quadrada de {} é {:.3f}' .format(n, raiz))
