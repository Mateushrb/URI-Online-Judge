# Definição da variável necessária
valores_pares = 0

# Estrutura de repetição com condição
for i in range(0, 5):
    valor = int(input()) # Entrada
    if valor%2 == 0: # Condição
        valores_pares += 1

# Saída de dados
print("%i valores pares" %valores_pares)
