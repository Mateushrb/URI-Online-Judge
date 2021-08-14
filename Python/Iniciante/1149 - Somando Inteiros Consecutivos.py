# Entrada de variáveis na forma de lista
variaveis = list(int(x) for x in input().split())

# A possui o valor cujo índice é 0 (zero)
A = variaveis[0]

# Estrutura de repetição para escolher valor de N maior do que 0 (zero)
for i in range(len(variaveis)-1):
    # Condição para valor de N
    if variaveis[i+1] > 0:
        N = variaveis[i+1]
        break

# Variáveis necessarias para soma
i = 0
soma = 0

# Estrutura de repetição para somar os valores
while i != (N):
    soma += A + i
    i += 1

# Impressão do resultado
print(soma)
