# Tipo de cálculo
operacao = str(input())
# Declaração da matriz
M = []
# Estrutura de repetição para criação da matriz
for i in range(0, 12, 1):
    # Linha vazia
    linha = []
    # Estrutura de repetição para adicionar os elementos na linha
    for l in range(0, 12, 1):
        # Elemento
        elemento = float(input())
        # Adiciona o elemento na linha
        linha.append(elemento)
    # Adiciona a linha na matriz
    M.append(linha)
# Variáveis para realização do cálculo
calculo = 0
media = 0
# Estrutura de repetição para pegar os elementos solicitados
for j in range(1, 12, 1):
    for elementos in M[j][:j]:
        calculo += elementos
        media += 1
# Estrutura de seleção para realização dp cálculo solicitado
if operacao == 'S':
    print("%0.1f" %(calculo))
elif operacao == 'M':
    calculo /= media
    print("%0.1f" %(calculo))
else:
    pass

