#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o calor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, saendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
def aprovar_emprestimo(valor_casa, salario_comprador, anos_pagamento):
    prestacao_mensal = valor_casa / (anos_pagamento * 12)
    porcentagem_salario = (prestacao_mensal / salario_comprador) * 100

    if porcentagem_salario <= 30:
        print("Empréstimo aprovado!")
        print(f"Valor da prestação mensal: R${prestacao_mensal:.2f}")
    else:
        print("Empréstimo negado!")
        print(f"A prestação mensal de R${prestacao_mensal:.2f} excede 30% do seu salário.")

# Perguntar os dados
valor_casa = float(input("Digite o valor da casa: R$"))
salario_comprador = float(input("Digite o salário do comprador: R$"))
anos_pagamento = int(input("Digite em quantos anos o comprador vai pagar: "))

# Chamar a função
aprovar_emprestimo(valor_casa, salario_comprador, anos_pagamento)