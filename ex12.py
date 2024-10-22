#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.05
novo_preco = preco - desconto
print(f"O novo preço do produto em desconto é: R${novo_preco:.2f}")