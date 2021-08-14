# Quantidade de linhas
n = int(input())

# Estrutura de repetição
for i in range(0, n, 1):
    # Somar 1 pois i começa em 0
    i += 1
    # Criação da lista
    lista = []
    # Adição do primeiro valor
    lista.append(i)
    # Adição do segundo valor
    lista.append(i*i)
    # Adição do terceiro valor
    lista.append(lista[0]*lista[1])
    # Impressão do resultado
    print(*lista)
    # Somar 1 nos 2 últimos indices da lista
    lista[1] += 1
    lista[2] += 1
    print(*lista)
