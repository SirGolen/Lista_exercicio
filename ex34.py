#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1250, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%
# Leia os 3 números
# Pergunta o salário do funcionário
salario = float(input("Digite o salário do funcionário: "))

# Verifica se o salário é superior a R$ 1250
if salario > 1250:
    # Calcula o aumento de 10%
    aumento = salario * 0.10
else:
    # Calcula o aumento de 15%
    aumento = salario * 0.15

# Calcula o novo salário
novo_salario = salario + aumento

# Mostra o resultado
print("O aumento é de R$ {:.2f}".format(aumento))
print("O novo salário é de R$ {:.2f}".format(novo_salario))