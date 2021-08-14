# Estrutura de repetição
while True:
    # Entrada
    x = int(input())
    # Condição de parada e continuação
    if x == 0:
        break
    else:
        # Criação da lista
        lista = []
        # Variável para adicionar os números na lista
        numero = 0
        # Estrutura de repetição para adicionar os valores na lista
        while numero != x:
            # Somar 1
            numero += 1
            # Adicionar na lista
            lista.append(numero)
    # Imprimir o resultado
    print(*lista)
