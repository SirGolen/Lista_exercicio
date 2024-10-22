#Crie um programa que leie uma frase qualquer e diga se ela é um palindromo desconsiderando os espaços.
def verifica_palindromo(frase):
    frase_sem_espacos = frase.replace(" ", "").lower()
    return frase_sem_espacos == frase_sem_espacos[::-1]

frase = input("Digite uma frase: ")
if verifica_palindromo(frase):
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")