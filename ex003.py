# Vitor Hugo Otto

# Escrever um programa para calcular o volume de uma esfera sendo fornecido o valor de seu raio.

import math

raio = float(input("Nos informe o raio da esfera em questão: "))
vol = 4/3* math.pi *pow(raio,3)

print("O volume desta esfera é igual a %.2f unidades de medida" %vol)