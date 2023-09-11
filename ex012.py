# Vitor Hugo Otto

"""
Escrever um programa que leia o tempo de duração em segundos de um
determinado evento em uma fábrica e informe-o expresso no formato
horas:minutos:segundos.
"""

total_seg = int(input("Informe os segundos de duração da execução: "))

horas = total_seg // 3600

seg_restantes = total_seg % 3600
minutos = seg_restantes // 60

seg_restantes_final = seg_restantes % 60

print("%d:%d:%d" %(horas, minutos, seg_restantes_final))
