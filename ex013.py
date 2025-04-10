#Escreva um programa que converta uma températura digitada em ºC e a converta para ºF.

temp = int(input('Digite a temperatura: '))
far = (temp * 9 / 5) + 32
print('Sua temperatura de {}ºC ficará {}°F' .format(temp, far))
