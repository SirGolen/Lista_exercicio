#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# Leia o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Crie uma lista para armazenar os 10 primeiros termos da PA
termos = []

# Calcule e adicione os 10 primeiros termos da PA à lista
for i in range(10):
    termo = primeiro_termo + i * razao
    termos.append(termo)

# Mostre os 10 primeiros termos da PA
print("Os 10 primeiros termos da PA são:", termos)