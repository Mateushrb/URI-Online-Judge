# Estrutura de repetição com condição para parada
while True:
    # Leitura dos valores
    m, n = [int(x) for x in input().split()]
    # Condição se os valores forem maiores que zero, executa o programa
    if m > 0 and n > 0:
        if m > n: # Condição se M for maior que N
            soma = 0
            lista = list() # Lista para imprimir a sequencia dos valores
            # Estrutura de repetição para somar o valores
            while n <= m:
                soma += n
                lista.append(n) # Adiciona os valores da sequencia na lista
                n += 1
            print(*lista, "Sum=%i" %soma) # Imprimi o resultado
        else: # Condição se N for maior que M
            soma = 0
            lista = list() # Lista para imprimir a sequencia dos valores
            # Estrutura de repetição para somar o valores
            while m <= n:
                soma += m
                lista.append(m) # Adiciona os valores da sequencia na lista
                m += 1
            print(*lista, "Sum=%i" %soma) # Imprimi o resultado
    else: # Se algum dos valores for menor ou igual a zero
        break # Para o programa
