#Desenvolva um programa que leia as duas notas de um aluno, Calcule e mostre a sua média

nota1 = float(input("Digite a primeira nota aqui: "))
nota2 =  float(input("Digite a segunda nota: "))
media = (nota1 + nota2) /2
print("A média entre {} e {} é {}".format(nota1,nota2, media))