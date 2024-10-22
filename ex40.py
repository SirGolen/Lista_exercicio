#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem ao final, de acordo com a média atingida:
#Média abaixo de 5.0: Reprovado
#Média entre 5.0 e 6.9: Recuperação
#Média 7.0 ou superior: Aprovado

# Leia as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcule a média
media = (nota1 + nota2) / 2

# Mostre a mensagem de acordo com a média
if media < 5.0:
    print("Reprovado")
elif 5.0 <= media < 7.0:
    print("Recuperação")
else:
    print("Aprovado")