# Entrada de dados
a, b, c = [int(x) for x in input().split()]

# Cálculo
maiorAB = (a + b + abs(a - b)) / 2
maior = (maiorAB + c + abs(maiorAB - c)) / 2

# Saída de dados
print("%0.0f eh o maior" %maior)