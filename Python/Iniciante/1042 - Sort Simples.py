# Entrada de dados
a, b, c = [int(x) for x in input().split()]

# Organização

lista = list() # Criação da lista

lista.append(a) # Adicionar valor de a
lista.append(b) # Adicionar valor de b
lista.append(c) # Adicionar valor de c

lista.sort() # organizar em ordem crescente

# Saída de dados
for i in lista:
    print(i)
print()
print(a)
print(b)
print(c)