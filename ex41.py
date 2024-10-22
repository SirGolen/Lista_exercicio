#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 20 anos: Sênior
#Acima: Master
from datetime import date

def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade

def categoria_atleta(idade):
    if idade <= 9:
        return "Mirim"
    elif idade <= 14:
        return "Infantil"
    elif idade <= 19:
        return "Junior"
    elif idade <= 20:
        return "Sênior"
    else:
        return "Master"

ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
idade = calcular_idade(ano_nascimento)
categoria = categoria_atleta(idade)

print(f"O atleta tem {idade} anos e pertence à categoria {categoria}.")