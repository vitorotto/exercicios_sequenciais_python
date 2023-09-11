# Vitor Hugo Otto

# Escrever um programa que pergunte o nome de uma pessoa, o quanto ela
# por hora (salário por hora) e o número de horas trabalhadas no mês. Calcular
# e mostrar o total do seu salário no referido mês.

nome = input("Qual seu nome? ")
sal_h = float(input("%s, quanto você ganha por hora? " %nome))
hrs_mes = float(input("Quantas horas você trabalha por mês? "))

total = sal_h * hrs_mes

print("%s, seu salário total é de %.2f" %(nome, total))