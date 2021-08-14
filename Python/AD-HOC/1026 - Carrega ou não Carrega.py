# Estrutura de repetição infinita
while True:
    # Tente
    try:
        a, b = [int(x) for x in input().split()]
        # Conjunção lógica E ^
        mofiz = a^b
        print(mofiz)
    # Se não der, faça isto
    except EOFError:
        # Para o loop
        break
