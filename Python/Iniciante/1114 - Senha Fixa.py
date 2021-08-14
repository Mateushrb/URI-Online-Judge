senha = 2002
# Estrutura de repetição com condição de parada
while True:
    tentativa = int(input())
    if tentativa == senha:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
        continue
