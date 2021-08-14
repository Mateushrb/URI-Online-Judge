# Listas
par = list()
impar = list()
# Estrutura de repetição com seleções
for i in range(0, 15, 1):
    # Entrada do valor
    valor = int(input())
    # Condição para Par ou Ímpar
    if valor%2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    # Condição se atingir 5 itens na lista
    if len(par) == 5:
        # Estrutura de repetição para imprimir os 5 itens
        for l in range(0, 5, 1):
            print("par[%s] = %s" %(l, par[l]))
        # Zera a lista
        par = list()
    # Igual a condição aterior
    elif len(impar) == 5:
        for j in range(0, 5, 1):
            print("impar[%s] = %s" %(j, impar[j]))
        impar = list()
    # Não faz nada
    else:
        pass
# Estruturas de repetições para imprimir os itens que sobraram
for n in range(0, len(impar), 1):
    print("impar[%s] = %s" %(n, impar[n]))
for m in range(0, len(par), 1):
    print("par[%s] = %s" %(m, par[m]))
