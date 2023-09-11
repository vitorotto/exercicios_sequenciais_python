# Vitor Hugo Otto

'''
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
Supondo que a percentagem do distribuidor seja de 28% e os impostos 45%,
escrever um programa que leia o custo de fábrica de um carro e informe o
custo ao consumidor desse carro.
'''
custo_fabrica = float(input("Informe o preço do veículo: "))
imposto1 = custo_fabrica + (28/100)
imposto2 = custo_fabrica + (45/100)
custo_final = custo_fabrica + imposto1 + imposto2

print("O custo final do veículo é de R$%.2f com impostos aplicados" %custo_final)
