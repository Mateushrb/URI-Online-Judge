# Entrada de dados
tempo_gasto = int(input())
velocidade_media = int(input())

# Cálculo
# Autonomia do carro em KM/L
autonomia = 12
km_totais = tempo_gasto * velocidade_media

litros_gastos = km_totais / autonomia

# Saída de dados
print("%0.3f" %litros_gastos)