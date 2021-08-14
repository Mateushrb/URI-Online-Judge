# Valor inicial de S
s = 1
# Variável necessaria para o cálculo
divisor = 2
# Estrutura de repetição com os passos necessários
for i in range(3, 39, 2):
    s += i/divisor
    # Multiplicação do divisor
    divisor *= 2
# Impressão do resultado com formatação
print("%0.2f" %(s))
