# Variáveis para leitura dos valores
x = int(input())
y = int(input())

# # #
# Algorítimo para organizar em ordem crescente
menor = 0
maior = 0

# Condição para menor e maior
if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x
# # #

# Estrutura de repetição
for i in range(0, maior-menor-1, 1):
    # Adiciona 1 para o próximo teste
    menor += 1
    # Condições
    if menor%5 == 2 or menor%5 == 3:
        # Impressão dos resultados
        print(menor)
