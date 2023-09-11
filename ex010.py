# Vitor Hugo Otto

# Escrever um programa que leia dois pontos quaisquer no plano, p1(x1,y1) e
# p2(x2,y2) e calcule a distância entre eles.

import math

x1 = float(input("Entre com o valor de x1: "))
y1 = float(input("Entre com o valor de y1: "))

x2 = float(input("Entre com o valor de x2: "))
y2 = float(input("Entre com o valor de y2: "))

p1 = (x2 - x1) ** 2
p2 = (y2 - y1) ** 2

distancia = math.sqrt(p1 + p2)

print("A distância entre eles é de %.2f unidades de medida" %distancia)

