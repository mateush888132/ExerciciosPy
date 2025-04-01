#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros:

v = float(input('Adicione uma distância: '))
cm = v * 100
mm = v * 1000
print('A medida de {}m corresponde a {}cm e {}mm' .format(v, cm, mm))