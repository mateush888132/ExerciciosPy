#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com aumento de 15%.

sal = float(input('Digite seu salário para saber o aumento: '))
aum = sal * (15 / 100)
salfinal = sal + aum
print('O aumento do seu salário será R${:.2f} ficando no total R${:.2f}' .format(aum, salfinal))