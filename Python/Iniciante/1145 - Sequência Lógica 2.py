# Entrada de dados de forma linear
x, y = [int(x) for x in input().split()]

# Criação da lista
lista = list()

# Contador necessário para estrutura de repetição e contagem dos valores
contador = 1

# Estrutura de repetição
while contador != y+1:
    # Adiciona o valor do contador na lista
    lista.append(contador)
    # Soma 1 no contador
    contador += 1
    # Condição para impressão quado a lista tiver o valor de x
    if len(lista) == x:
        # Impressão da lista com o asterisco para remover os colchetes e virgulas
        print(*lista)
        # Apagar todos os valores da lista
        lista.clear()
# Condição para impressão quando a lista não tiver o valor de x
if len(lista) != 0:
    # Impressão da lista com o asterisco para remover os colchetes e virgulas
    print(*lista)
