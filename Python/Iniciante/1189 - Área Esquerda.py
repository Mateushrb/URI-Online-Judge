operacao = str(input())

matriz = list()
linha = list()
elemento = 0
# Criação da matriz
for i in range(0, 12, 1):
    linha = list()
    for l in range(0, 12, 1):
        elemento = float(input())
        linha.append(elemento)
    matriz.append(linha)

soma = 0
volta = 10
divisor = 0
# Pega os elementos solicitados
for n in range(1, 6, 1):
    for m in range(0, n, 1):
        soma += matriz[n][m] # n pode ser a ida pois começa em 1
        soma += matriz[volta][m]
        divisor += 2
    volta -= 1
# Impressão do resultado
if operacao == 'S':
    print("%0.1f" %(soma))
elif operacao == 'M':
    print("%0.1f" %(soma/divisor))
else:
    pass
