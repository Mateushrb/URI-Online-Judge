# Variáveis de contagem
v_pares = 0
v_impares = 0
v_positivos = 0
v_negativos = 0

# Estrutura de repetição com condições
for i in range(0, 5, 1):
    valor = int(input()) # Entrada
    if valor%2 == 0: # Condição
        v_pares += 1
    else:
        v_impares += 1
    if valor > 0: # Condição
        v_positivos += 1
    if valor < 0: # Condição
        v_negativos += 1

# Impressão dos resultados
print("%i valor(es) par(es)" %v_pares)
print("%i valor(es) impar(es)" %v_impares)
print("%i valor(es) positivo(s)" %v_positivos)
print("%i valor(es) negativo(s)" %v_negativos)
