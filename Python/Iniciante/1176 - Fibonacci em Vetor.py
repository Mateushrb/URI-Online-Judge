# Lista da sequencia inicial de Fibonacci
sequencia_fibo = [0, 1]
valor_fibo = 0
# Estrutura de repetição para calcular a sequencia de Fibonacci
for i in range(0, 60, 1):
    valor_fibo = sequencia_fibo[i] + sequencia_fibo[i+1]
    sequencia_fibo.append(valor_fibo)
# Quantidade de testes
T = int(input())
casos_testes = list()
# Estrutura de repetição para adicionar os casos de testes na lista
for l in range(0, T, 1):
    N = int(input())
    casos_testes.insert(l, N)
# Estrutura de repetição para imprimir os testes
for m in casos_testes:
    print("Fib(%s) = %s" %(m, sequencia_fibo[m]))
