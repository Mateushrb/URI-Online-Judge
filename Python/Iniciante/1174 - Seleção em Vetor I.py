# Declaração da lista
vetor = list()
# Estrutura de repetição para adicionar os valores na lista
for i in range(0, 100, 1):
    valor = float(input())
    vetor.insert(i, valor)
# Estrutura de repetição com seleção para impressão
for l in range(0, 100, 1):
    if vetor[l] <= 10:
        print("A[{indice}] = {valor}".format(indice=l, valor=vetor[l]))
    else:
        # "pass" não faz nada
        pass
