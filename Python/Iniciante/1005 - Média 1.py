# Entrada de dados
A = float(input())
B = float(input())

# Pesos
peso_a = 3.5
peso_b = 7.5

# Cálculo
media = (A*peso_a + B*peso_b) / (peso_a + peso_b)

# Arredondamento
m = round(media, 5)

# Saída de dados
print("MEDIA = %0.5f" %m)