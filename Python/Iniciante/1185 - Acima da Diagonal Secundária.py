# Tipo de operação
operacao = str(input())
# declaração da matriz
M = list()
# Estrutura de repetição para criação da matriz
for i in range(0, 12, 1):
    # Lista vazia
    linha = list()
    # Estrutura de repetição para adicionar as linhas na matriz
    for l in range(0, 12, 1):
        # Entrada do elemento
        elemento = float(input())
        # Adiciona o elemento na linha
        linha.append(elemento)
    # Adiciona a linha na matriz
    M.append(linha)
# Variáveis para o cálculo
calculo = 0
media = 0
# Estrutura de repetição para pegar os elementos solicitados
for j in range(1, 12, 1):
    for elementos in M[j-1][:-j]:
        calculo += elementos
        media += 1
# Estrutura de seleção para realização do cálcul
if operacao == 'S':
    print("%0.1f" %(calculo))
elif operacao == 'M':
    calculo /= media
    print("%0.1f" %(calculo))
else:
    pass
