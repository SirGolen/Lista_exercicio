# Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
tinta = area / 2
print(f"A área da parede é {area}m² e a quantidade de tinta necessária é {tinta}L")

