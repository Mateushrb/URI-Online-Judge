# Entrada de dados
a, b, c = [float(x) for x in input().split()]

# Cálculo
delta = b**2 - 4*a*c
if delta**0.5 == b or delta <=0:
    print("Impossivel calcular")
else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("R1 = %0.5f" %x1)
    print("R2 = %0.5f" %x2)
