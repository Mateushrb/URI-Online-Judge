# Valores
A, B, C = [float(x) for x in input().split()]

# Lista
ordem = list()

# Adição dos valores
ordem.append(A)
ordem.append(B)
ordem.append(C)

# Valores em ordem decrecente
ordem.sort(reverse = True)

# Alteração dos valores das variáveis
A = ordem[0]
B = ordem[1]
C = ordem[2]

# Condições
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if A == B != C or A != B == C:
        print("TRIANGULO ISOSCELES")
