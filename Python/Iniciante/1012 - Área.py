# Entrada de dados
A, B, C = [float(x) for x in input().split()]
pi = 3.14159

# Cálculo
area_triangulo = (A * C) / 2
area_circulo = pi * (C**2)
area_trapezio = ((A + B) / 2) * C
area_quadrado = B * B
area_retangulo = A * B

# Saída de dados
#print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO %0.3f" %(area_triangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo))
print("TRIANGULO: %0.3f" %area_triangulo)
print("CIRCULO: %0.3f" %area_circulo)
print("TRAPEZIO: %0.3f" %area_trapezio)
print("QUADRADO: %0.3f" %area_quadrado)
print("RETANGULO: %0.3f" %area_retangulo)