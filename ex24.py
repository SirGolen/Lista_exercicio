#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
cidade = input("Digite o nome da cidade: ")

if cidade.upper().startswith("SANTO"):
    print("A cidade começa com 'SANTO'!")
else:
    print("A cidade não começa com 'SANTO'.")