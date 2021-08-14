# Valor de entrada
n = int(input())

# Divisores
divisor = 1

# Estrutura de repetição
while divisor < 10000:
    if divisor % n == 2: # Condição 
        print(divisor) # Saída
    divisor += 1
