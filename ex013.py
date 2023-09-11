# Vitor Hugo Otto

"""
Escrever um programa que leia o tempo inicial e final de uma partida de tênis
no formato hor:min:seg e informe o tempo de duração da mesma no formato
hor:min:seg.
"""
print("Informe o inicio do evento:")
hi = int(input("Informe as horas iniciais: "))
mi = int(input("Informe os minutos iniciais: "))
si = int(input("Informe os segundos iniciais: "))
print("Informe o final do evento:")
hf = int(input("Informe as horas finais: "))
mf = int(input("Informe os minutos finais: "))
sf = int(input("Informe os segundos finais: "))

#Inicio - Conversão:
segs_inicio = (hi * 3600) + (mi * 60) + si

#Final - conversão:
segs_final = (hf * 3600) + (mf * 60) + si

#Duração do evento em segundos:
tempo_durac = segs_final - segs_inicio

#Passando para o formato correto:
hora = tempo_durac // 3600
resto = tempo_durac % 3600
minuto = resto // 60
segundo = resto % 60

print("A duração do evento foi de %.d:%.d:%.d" %(hora, minuto, segundo))


