# Entrada de dados
A = float(input())
B = float(input())
C = float(input())

# Pesos
peso_a = 2
peso_b = 3
peso_c = 5

# Cálculo
media = (A*peso_a + B*peso_b + C*peso_c) / (peso_a + peso_b + peso_c)
m = round(media, 1)

# Saída de dados
print("MEDIA = %0.1f" %m)