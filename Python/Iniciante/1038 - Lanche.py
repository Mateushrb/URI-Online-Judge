# Dados de entrada
codigo, quantidade = [int(x) for x in input().split()]

# Cálculo
lista = [4, 4.5, 5, 2, 1.5]
pedido = lista[codigo-1]*quantidade

# Saída de dados
print("Total: R$ %0.2f" %pedido)