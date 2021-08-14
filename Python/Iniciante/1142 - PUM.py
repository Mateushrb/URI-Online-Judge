# Quantidade de linhas
N = int(input())

# Variável necessária para contagem dos valores
valores = 0

# Estrutura de repetição
for i in range(0, N, 1):
    # Variável do PUM
    valores += 1
    # Criação de lista para adição dos valores e facilitar a impressão
    lista = []
    # Estrutura de repetição para adição dos valores
    for i in range(3):
        lista.append(valores)
        valores += 1
    # Adição do PUM na lista
    lista.append("PUM")
    # Impressão do resultado
    print(*lista) # Asterisco remove os colchetes e virgulas da lista
