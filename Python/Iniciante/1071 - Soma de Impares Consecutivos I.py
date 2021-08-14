# Entrada de dados
x = int(input())
y = int(input())

# Condição para número impar e para ficar entre os valores
if y%2 == 0:
    y += 1
else:
    y += 2

# Variável de soma
soma = 0

# Estrutura de repetição
while y < x:
    soma += y
    y += 2

# Impressão do resultado
print(soma)
