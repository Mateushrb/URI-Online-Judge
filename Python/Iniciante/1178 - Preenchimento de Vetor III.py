# Valor inicial
X = float(input())
# Lista
N = list()
# Adicionar valor inicial
N.append(X)
# Estrutura de repetição para adicionar os valores
for i in range(1, 100, 1):
    # Dividir por 2
    X /= 2
    # Adicionar valor
    N.append(X)

# Estrutura de repetição para imprimir a lista
for i in range(0, len(N), 1):
    print("N[%s] = %0.4f" %(i, N[i]))
