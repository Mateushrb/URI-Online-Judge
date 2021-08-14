# Linha do cálculo
linha_operacao = int(input())
# Tipo de cálculo
operacao = str(input())
# Ciação da lista
M = list()
# Estrutura de repetição para criar a matriz
for i in range(0, 12, 1):
    # Cria uma lista vazia
    linha = list()
    # Adiciona os elemenos na lista
    for l in range(0, 12, 1):
        elemento = float(input())
        linha.append(elemento)
    # Adiciona a lista dentro da lista anterior
    M.append(linha)
# Variável utilizada para o cálculo
resultado = 0
# Operação de Soma
if operacao == 'S':
    # Percorre a linha (iteração) e soma os elementos na variável resultado
    for j in M[linha_operacao]:
        resultado += j
    # Imprime o resultado
    print("%0.1f" %(resultado))
# Operação de Média
elif operacao == 'M':
    # Percorre a linha (iteração) e soma os elementos na variável resultado
    for j in M[linha_operacao]:
        resultado += j
    # Calcula a média
    resultado /= 12
    # Imprime o resultado
    print("%0.1f" %(resultado))
