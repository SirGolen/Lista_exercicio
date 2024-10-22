# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
n = int(input('Digite um número: '))
print(f'Tabuada do {n}:')
for c in range(1, 11):
    print(f'{n} x {c} = {n * c}')