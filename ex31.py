#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200 Km e R$ 0.45 para viagens mais longas
# Pergunta a distância da viagem em Km
distancia_km = float(input("Digite a distância da viagem em Km: "))

# Calcula o preço da passagem
if distancia_km <= 200:
    preco_passagem = distancia_km * 0.50
else:
    preco_passagem = distancia_km * 0.45

# Mostra o resultado
print(f"O preço da passagem é R${preco_passagem:.2f}")