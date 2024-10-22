#Crie um programa que leia o ano de nascimento de 7 pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

# Função para calcular a idade
def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    return ano_atual - ano_nascimento

# Inicializar contadores
maiores = 0
menores = 0

# Ler anos de nascimento de 7 pessoas
for i in range(7):
    ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {i+1}: "))
    idade = calcular_idade(ano_nascimento)
    
    # Verificar se a pessoa é maior ou menor de idade
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

# Mostrar resultados
print(f"Quantidade de pessoas maiores de idade: {maiores}")
print(f"Quantidade de pessoas menores de idade: {menores}")