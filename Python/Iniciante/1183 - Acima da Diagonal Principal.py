# Tipo de cálculo
operacao = str(input())
# Declaração da matriz
M = []
# Estrutura de repetição para adicionar as linhas da matriz
for i in range(0, 12, 1):
    # Declaração da linha
    linha = []
    # Estrutura de repetição para adicionar os elementos na linha
    for l in range(0, 12, 1):
        # Entrada de dados
        elemento = float(input())
        # Adiciona o elemento na linha
        linha.append(elemento)
    # Adiciona a linha na matriz
    M.append(linha)
    
calculo = 0
media = 0
# Pega os elementos da área solicitada e soma na variável cálculo
for j in range(0, 11, 1):
    elementos = M[j][j+1:]
    for l in elementos:
        calculo += l
        media += 1
# Estrutura de seleção para o tipo de operação
if operacao == 'S':
    print("%0.1f" %(calculo))
elif operacao == 'M':
    calculo /= media
    print("%0.1f" %(calculo))
else:
    pass
