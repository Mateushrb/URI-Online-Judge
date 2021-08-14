# Valor inicial de S
S = 1

# Estrutura de repetição
for i in range(2, 101, 1):
    # Soma a "S" 1 dividido por "i", no qual "i" começa em 2
    # e e vai aumentando gradualmente através da estrutura de repetição
    S += 1/i

# Impressão do resultado com formatação
print("%0.2f" %(S))
