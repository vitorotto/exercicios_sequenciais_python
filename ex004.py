# Vitor Hugo Otto 

# Escrever um programa que leia o nome de um aluno e as notas das 3 provas
# que ele obteve no semestre. No final informar o nome do aluno e a sua
# média (aritmética).

nome = input("Olá! Por favor digite seu nome: ")
prova1 = float(input("Informe o resultado da sua primeira prova: "))
prova2 = float(input("Informe o resultado da sua segunda prova: "))
prova3 = float(input("Informe o resultado da sua terceira prova: "))

media = (prova1 + prova2 + prova3) / 3

print(" %s, sua média foi de %.2f" %(nome, media))