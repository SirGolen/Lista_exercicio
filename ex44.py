#Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
def calcular_valor_pago(preco_normal, forma_pagamento, quantidadeparcelas=1):
    if forma_pagamento == "dinheiro" or forma_pagamento == "cheque":
        return preco_normal * 0.9  # 10% de desconto
    elif forma_pagamento == "cartao_a_vista":
        return preco_normal * 0.95  # 5% de desconto
    elif forma_pagamento == "cartao_2x":
        return preco_normal  # preço normal
    elif forma_pagamento == "cartao_3x_ou_mais" and quantidadeparcelas >= 3:
        return preco_normal * 1.2  # 20% de juros
    else:
        return "Forma de pagamento inválida"

# Exemplo de uso:
preco_normal = 100.0
forma_pagamento = "cartao_3x_ou_mais"
quantidadeparcelas = 3

valor_pago = calcular_valor_pago(preco_normal, forma_pagamento, quantidadeparcelas)
print(f"O valor a ser pago é R$ {valor_pago:.2f}")