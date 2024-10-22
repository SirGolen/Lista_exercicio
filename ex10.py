# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar . Considere US$1,00 = R$3.27

def conversao_reais_dolares(reais):
    return reais / 3.27

def main():
    valor_reais = float(input("Quantos reais você tem? R$"))
    valor_dolares = conversao_reais_dolares(valor_reais)
    print(f"Você pode comprar {valor_dolares} dólares")
main()


