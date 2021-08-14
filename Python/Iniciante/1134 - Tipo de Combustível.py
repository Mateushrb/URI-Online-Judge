# Variável de indicação de combustível
combustivel = 0

# Variáveis para contagem
alcool = 0
gasolina = 0
diesel = 0

# Estrutura de repetição com condição de parada (se for igual a 4)
while combustivel != 4:
    # Tipo de combustível
    combustivel = int(input())
    # Estrutura de repetição para caso o tipo de combustível seja inválido
    while combustivel < 1 or combustivel > 4:
        combustivel = int(input())
    # Condições para contagem de clientes
    if combustivel == 1:
        alcool += 1
    elif combustivel == 2:
        gasolina += 1
    elif combustivel == 3:
        diesel += 1

# Impressão dos resultados
print("MUITO OBRIGADO")
print("Alcool: %s" %(alcool))
print("Gasolina: %s" %(gasolina))
print("Diesel: %s" %(diesel))
