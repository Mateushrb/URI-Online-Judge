# Valores
A, B = [int(x) for x in input().split()]

# Cálculo
if A > B:
    multiplo = int(A / B)
    if multiplo * B == A:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    multiplo = int(B / A)
    if multiplo * A == B:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
