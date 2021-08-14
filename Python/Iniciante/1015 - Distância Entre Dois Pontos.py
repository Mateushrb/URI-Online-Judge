# Entrada de dados
x1, y1 = [float(x) for x in input().split()]
x2, y2 = [float(x) for x in input().split()]

# Cálculo
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Saída de dados
print(round(distancia, 4))