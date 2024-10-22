#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezez aparece a letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = input("Digite uma frase: ")

contador_a = 0
primeira_posicao = -1
ultima_posicao = -1

for i, letra in enumerate(frase):
    if letra.upper() == 'A':
        contador_a += 1
        if primeira_posicao == -1:
            primeira_posicao = i
        ultima_posicao = i

print(f"A letra 'A' aparece {contador_a} vezes na frase.")
print(f"A letra 'A' aparece pela primeira vez na posição {primeira_posicao}.")
print(f"A letra 'A' aparece pela última vez na posição {ultima_posicao}.")