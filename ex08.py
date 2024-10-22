#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metro = float(input("Digite um valor em metros: ")) 
centimetro = metro * 100
milimetro = metro * 1000
print(f"{metro} metro(s) é igual a {centimetro} centimetro(s) é igual a {milimetro}")
