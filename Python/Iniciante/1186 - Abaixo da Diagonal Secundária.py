operacao = input()
matriz = list()
# Estrutura de repetição para criação da matriz
for i in range(0, 12, 1):
    linha = list()
    for l in range(0, 12, 1):
        elemento = float(input())
        # Adiciona o elemento na linha
        linha.append(elemento)
    # Adiciona a linha na matriz
    matriz.append(linha)
soma = 0
elementos = 12
divisor = 0
# Pega os elementos solicitados
for j in range(1, 12, 1):
    elementos -= 1
    for k in range(elementos, 12, 1):
        soma += matriz[j][k]
        divisor += 1
# Imprime o resultado
if operacao == 'S':
    print("%0.1f" %(soma))
elif operacao == 'M':
    media = soma/divisor
    print("%0.1f" %(media))
else:
    pass
