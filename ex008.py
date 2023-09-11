# Vitor Hugo Otto

# Escrever um programa que leia o nome de um vendedor, o seu salário fixo e
# o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este
# vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o
# seu salário no final do mês.

nome = input("Qual seu nome? ")
sal_fixo = float(input("Qual seu salário fixo? "))
vendas = float(input("Qual o seu total, em dinheiro, de vendas efetuadas este mês? "))
comissao = vendas * (15/100)

sal_final = sal_fixo + comissao

print(nome, "seu salário final será de: R$%.2f" %sal_final)