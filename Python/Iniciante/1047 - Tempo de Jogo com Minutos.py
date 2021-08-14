# Entrada de dados
h_inicial, m_inicial, h_final, m_final = [int(x) for x in input().split()]

# Cálculo das horas
horas = h_final - h_inicial
if horas < 0 :
    horas += 24

# Cálculo dos minutos
minutos = m_final - m_inicial
if minutos < 0:
    minutos += 60
    horas -= 1
    if horas < 0:
        horas += 24
    
# Resultado
if minutos == horas == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(horas, minutos))
