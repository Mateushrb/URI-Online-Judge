# Declaração da lista
vetor = list()
# Estrutura de repetição para adicionar os valores
for i in range(0, 20, 1):
    valor = int(input())
    vetor.insert(i, valor)
# Variáves
anterior = 0
posterior = 0
# Estrutura de repetição para inverter
for l in range(0, 10, 1):
    # remove o valor da lista e coloca na variável
    anterior = vetor.pop(l)
    posterior = vetor.pop(18-l)
    # Insere o valor da variável na posição indicada
    vetor.insert(l, posterior)
    vetor.insert(19-l, anterior)
# Estrutura de repetição para imprimir o resultado
for n in range(0, 20, 1):
    print("N[{indice}] = {valor}".format(indice = n, valor = vetor[n]))
