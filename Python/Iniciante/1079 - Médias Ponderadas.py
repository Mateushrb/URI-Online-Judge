# Número de casos de teste
n = int(input())

# Estrutura de repetição
for i in range(0, n, 1):
    v1, v2, v3 = [float(x) for x in input().split()]
    media = (v1*2 + v2*3 + v3*5) / (10)
    print(round(media, 1))
