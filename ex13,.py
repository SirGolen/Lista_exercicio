#Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite o salario do funcionário: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f"O novo salario do funcionário é: R${novo_salario:.2f}")