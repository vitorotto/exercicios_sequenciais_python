# Vitor Hugo Otto

# Escrever um programa para determinar o consumo médio de um automóvel
# sendo fornecidos a distância total percorrida pelo automóvel e o total de
# combustível gasto.

km = float(input("Informe a quilometragem percorrida: "))
l = float(input("Quantos litros de combustível foram gastos? "))

media = km / l

print("A média de consumo é %.2f km/l" %media)