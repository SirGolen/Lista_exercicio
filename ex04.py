#Faça um programa que leia algo pelo teclado e mostre na tela do seu tipo primitivo e todas as informações possíveis sobre ele
#ex: nome=Flávio, tipo=string, quantidade de caracteres=6, etc
entrada = input("Digite algo: ")

print("Nome:", entrada)
print("Tipo:", type(entrada))
print("Quantidade de caracteres:", len(entrada))

if entrada.isalpha():
    print("É uma string apenas com letras")
elif entrada.isdigit():
    print("É uma string apenas com números")
else:
    print("É uma string mista")

if entrada.isspace():
    print("É uma string vazia ou contém apenas espaços")
else:
    print("Não é uma string vazia")

print("Maiúscula:", entrada.isupper())
print("Minúscula:", entrada.islower())
print("Capitalizada:", entrada.istitle())