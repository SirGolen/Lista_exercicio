#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-0
soma = 0
for i in range(6):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        soma += num
print("A soma dos números pares é:", soma)