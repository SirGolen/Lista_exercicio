#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome_completo = input("Digite seu nome completo: ")

nome_maiusculo = nome_completo.upper()
print("Nome com todas as letras maiúsculas:", nome_maiusculo)

nome_minusculo = nome_completo.lower()
print("Nome com todas as letras minúsculas:", nome_minusculo)

letras_totais = len(nome_completo.replace(" ", ""))
print("Quantas letras ao todo (sem considerar espaços):", letras_totais)

primeiro_nome = nome_completo.split()[0]
letras_primeiro_nome = len(primeiro_nome)
print("Quantas letras tem o primeiro nome:", letras_primeiro_nome)
