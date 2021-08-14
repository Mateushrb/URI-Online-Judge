# Quantidade de casos
NC = int(input())
# Estrutura de repetição
for i in range(0, NC, 1):
    # Entrada de dados
    n, k = [int(x) for x in input().split()]
    # Lista sequencial de 1 até n
    roda = [x for x in range(1, n+1)]
    # Variável para remover um elemento da lista
    matador = k - 1
    # Estrutura de repetição até sobrar 1 na lista
    while len(roda) > 1:
        # Se a variável matador for maior que a quantidade de elementos na lista
        if matador >= len(roda):
            # Divide a variável pelo tamanho da lista e atribui o resto a variável
            matador %= len(roda)
        # Remove da lista o elemento cujo indice é "matador"
        roda.pop(matador)
        # Adiciona (k-1) na variável matador
        matador += (k - 1)
    # Imprime o resultado
    print(f'Case {i+1}: {roda[0]}')
