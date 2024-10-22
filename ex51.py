#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
def é_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Digite um número inteiro: "))
if é_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")