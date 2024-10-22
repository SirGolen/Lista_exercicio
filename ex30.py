#Crie um programa que leia o número inteiro e mostre na tela se ele é PAR ou IMPAR

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é IMPAR.")