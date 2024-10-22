#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# Pedir ao usuário para digitar um número
num = int(input("Digite um número para ver sua tabuada: "))

# Criar a tabuada utilizando um laço for
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")