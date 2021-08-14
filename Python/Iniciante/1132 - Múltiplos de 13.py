# Entrada de dados
x = int(input())
y = int(input())

# Variáveis menor e maior
menor = 0
maior = 0

# Condição para definir menor e maior
if x > y:
    maior = x
    menor = y
else:
    menor = x
    maior = y

# Variável para somar os resultados
soma = 0

# Estrutura de repetição para encontrar os valores que não são múltiplos de 13
for i in range(0, maior-menor+1, 1):
    # Condição para valores não múltiplos
    if menor%13 != 0:
        soma += menor
    # Adicionar +1 na variável menor para testar o próximo número
    menor += 1

print(soma) # Impressão do resultado
