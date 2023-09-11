# Vitor Hugo Otto

# Escrever um programa que leia as 3 notas de um aluno e calcule a média
# final deste aluno. Considerar que a média é ponderada e que os pesos das
# notas são: 2,3 e 5, respectivamente.

p1 = float(input("Escreva o resultado da sua primeira prova: "))
p2 = float(input("Escreva o resultado da sua segunda prova: "))
p3 = float(input("Escreva o resultado da sua terceira prova: "))

media = ((2*p1) + (3*p2) + (5*p3)) / (2 + 3 + 5)

print("Sua média foi igual a %.2f" %media)