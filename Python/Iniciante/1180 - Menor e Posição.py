# Importar módulo matemático 
import math
# Entrada de dados
N = int(input())
X = [int(x) for x in input().split()]
# Iniciar menor valor como infinito através do módulo matemático
menor_valor = math.inf
# Estrutura de iteração com seleção
for i in X:
    # Condição para menor valor
    if i < menor_valor:
        menor_valor = i
# Impressão dos resultados
print("Menor valor: %s" %(menor_valor))
print("Posicao: %s" %(X.index(menor_valor)))
