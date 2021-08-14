# Definição da variável
cont = 0

# Estrutura de repetição com condição
for i in range(6):
    valor = float(input()) # Entrada de dados
    if valor > 0: # Condição
        cont += 1
# Impressão do resultado
print("%i valores positivos" %cont)
