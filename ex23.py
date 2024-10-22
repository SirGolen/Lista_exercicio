#Faça um programa que leia um número e mostre na tela cada um dos digitos separados.
#EX:
#Digite um número: 1834
#Unidade:4
#Dezena:3
#Centena:8
#Milhar:1
n = int(input("Digite um número: "))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f" Unidade: {u}", f"Dezena: {d}", f"Centena: {c}", f"Milhar: {m}")