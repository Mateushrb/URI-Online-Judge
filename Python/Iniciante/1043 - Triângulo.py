# Medidas
A, B, C = [float(x) for x in input().split()]

# Condição de existencia do triângulo
c1 = abs(B - C) < A
c2 = B + C > A

if c1 == True and c2 == True:
    perimetro = A + B + C
    print("Perimetro = %0.1f" %perimetro)
else:
    area = ((A + B) / 2) * C
    print("Area = %0.1f" %area)
