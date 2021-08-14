# Coluna do cálculo
coluna_operacao = int(input())
# Tipo de cálculo
operacao = str(input())
# Declaração da lista
M = list()
# Estrutura de repetição para criação da matriz
for i in range(0, 12, 1):
    # Criação de uma lista vazia
    linha = list()
    # Estrutura de repetição para adicionar os elementos na linha i
    for l in range(0, 12, 1):
        elemento = float(input())
        linha.append(elemento)
    # Adiciona a linha na matriz
    M.append(linha)
# Variável necessária para o cálculo
resultado = 0
# Estrutura de repetição para somar os elementos da coluna na variável resultado
for j in range(0, 12, 1):
    resultado += M[j][coluna_operacao]
# Estrutura de seleção para o tipo de cálculo
if operacao == "S": # Soma
    print("%0.1f" %(resultado))
elif operacao == "M": # Média
    resultado /= 12
    print("%0.1f" %(resultado))
else: # Não faz nada
    pass
