#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres tem menos de 20 anos.
pessoas = []

for i in range(4):
    nome = input("Digite o nome da pessoa {}: ".format(i+1))
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
    sexo = input("Digite o sexo da pessoa {} (M/F): ".format(i+1)).upper()

    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})

# Cálculo da média de idade
soma_idades = sum(pessoa["idade"] for pessoa in pessoas)
media_idade = soma_idades / len(pessoas)

# Encontrar o homem mais velho
homem_mais_velho = max((pessoa for pessoa in pessoas if pessoa["sexo"] == "M"), key=lambda x: x["idade"])

# Contar mulheres com menos de 20 anos
mulheres_menos_20 = sum(1 for pessoa in pessoas if pessoa["sexo"] == "F" and pessoa["idade"] < 20)

print("Média de idade do grupo: {:.2f}".format(media_idade))
print("Homem mais velho: {}".format(homem_mais_velho["nome"]))
print("Mulheres com menos de 20 anos: {}".format(mulheres_menos_20))