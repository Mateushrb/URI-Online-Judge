# Criação do vetor (lista)
vetor = list()

# Estrutura de repetição para adicionar os valores na lista
for i in range(0, 10, 1):
    # Entrada de dado
    x = int(input())
    # Condição para valores nulos e negativos
    if x <= 0:
        vetor.append(1)
    else:
        vetor.append(x)

# Estrutura de repetição para imprimir os valores
for i in range(0, 10, 1):
    print("X[%s] = %s" %(i, vetor[i]))
