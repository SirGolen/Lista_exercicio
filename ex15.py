#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km_percorridos = float(input("Quantos Km foram percorridos? "))
dias_alugados = float(input("Quantos dias o carro foi alugado? "))
preco_dia = 60
preco_km = 0.15
preco_total = (preco_dia * dias_alugados) + (preco_km * km_percorridos)
print(f"O preço total a pagar é de R${preco_total:.2f}")
