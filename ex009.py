# Vitor Hugo Otto

# Escrever um programa que leia 3 valores inteiros e calcule as raízes da
# equação de báscara.

import math

a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
c = int(input("Qual o valor de c? "))

delta = pow(b,2) - 4 * a * c

raiz1 = (-b + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2 * a)

print("Raiz 01 = %.1f e raiz 02 = %.1f" %(raiz1, raiz2))
