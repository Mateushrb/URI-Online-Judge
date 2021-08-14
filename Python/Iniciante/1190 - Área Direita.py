O = str(input())

matriz = list()
linha = list()

for i in range(0, 12, 1):
    for j in range(0, 12, 1):
        elemento = float(input())
        linha.append(elemento)
    matriz.append(linha)
    linha = []

soma = 0
divisor = 0
limite = 10

for m in range(1, 11, 1):
    for n in range(11, limite, -1):
        soma += matriz[m][n]
        divisor += 1
    if m < 5:
        limite -= 1
    elif m > 5:
        limite += 1

if O == 'S':
    print("%0.1f" %(soma))
elif O == 'M':
    media = soma/divisor
    print("%0.1f" %(media))
