#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente  de um triangulo retângulo,
#calcule e mostre o comprimento da hipotenusa
import math

cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print("Comprimento da hipotenusa: ", hipotenusa)