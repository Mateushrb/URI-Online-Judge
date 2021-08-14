# Entrada
d_inicio = input().split()
d_inicio = int(d_inicio[1])

t_inicio = input().split()
h_inicio = int(t_inicio[0])
m_inicio = int(t_inicio[2])
s_inicio = int(t_inicio[4])

d_final = input().split()
d_final = int(d_final[1])

t_final = input().split()
h_final = int(t_final[0])
m_final = int(t_final[2])
s_final = int(t_final[4])

# Cálculo
d_duracao = d_final - d_inicio - 1
if h_inicio < h_final:
    d_duracao += 1
else:
    if h_inicio == h_final:
        if m_inicio < m_final:
            d_duracao += 1
        else:
            if m_inicio == m_final:
                if s_inicio < s_final:
                    d_duracao += 1
if d_duracao < 0:
    d_duracao += 1

h_duracao = h_final - h_inicio
if h_duracao < 0:
    h_duracao += 24

m_duracao = m_final - m_inicio
if m_duracao < 0:
    m_duracao += 60
    h_duracao -= 1
    if h_duracao < 0:
        h_duracao += 24

s_duracao = s_final - s_inicio
if s_duracao < 0:
    s_duracao += 60
    m_duracao -= 1
    if m_duracao < 0:
        m_duracao += 60
        h_duracao -= 1
        if h_duracao < 0:
            h_duracao += 24

# Resultado
print("%i dia(s)" %d_duracao)
print("%i hora(s)" %h_duracao)
print("%i minuto(s)" %m_duracao)
print("%i segundo(s)" %s_duracao)
