# Variáveis necessárias
valores_positivos = 0
soma_positivos = 0

# Estrutura de repetição com condição
for i in range(0, 6):
    valor = float(input()) # Entrada de dados
    if valor > 0: # Condição
        valores_positivos += 1
        soma_positivos += valor
# Cálculo da média
media = round(soma_positivos/valores_positivos, 1)

# Saída de dados
print("%i valores positivos" %valores_positivos)
print(media)
