# Entrada de dados
A, B, C, D = [int(x) for x in input().split()]

# Seleção
if B > C and D > A:
    if C + D > A + B:
        if C > 0 and D > 0:
            if A%2==0:
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")
